(ns _ (:require [clojure.string :as str] [clojure.test :as test]))

(defn expt
  ([x y] (expt x y 1))
  ([x y acc] (if (= y 0) acc (recur x (dec y) (* acc x)))))
(test/testing
  (test/is (= (expt 2 0) 1))
  (test/is (= (expt 2 1) 2))
  (test/is (= (expt 2 2) 4)))

(def lns (str/split-lines (slurp "fourteen.txt")))


(defn bin->int
  ([b] (bin->int (seq b) (dec (count b)) 0))
  ([b n acc]
   (if (empty? b)
     acc
     (recur (rest b) (dec n) (+ acc (* (if (= (first b) \1) 1 0) (expt 2 n)))))))
(test/testing
  (test/is (= (bin->int "111") 7))
  (test/is (= (bin->int "111") 7))
  (test/is (= (bin->int "1111") 15))
  (test/is (= (bin->int "101") 5))
  (test/is (= (bin->int "000") 0)))

(defn int->bin
  ([i] (str/join (int->bin i 0 35 [])))
  ([i acc n b]
   (if (< n 0)
     b
    (let
      [j (+ acc (expt (bigint 2) (bigint n)))]
      (if (> j i)
        (recur i acc (dec n) (conj b 0))
        (recur i j (dec n) (conj b 1)))))))
(test/testing
  (test/is (str/ends-with? (int->bin 2) "0000010"))
  (test/is (str/ends-with? (int->bin 5) "101")))

(defn
  ^{:test (fn []
              (assert (= (apply-mask "XXX1" "0000") "0001"))
              (assert (= (apply-mask "XXX1" "0") "0001"))
              (assert (= (apply-mask "XXX0" "0") "0000"))
              (assert (= (apply-mask "XXX1" "0010") "0011"))
              (assert (= (apply-mask "XX01" "0010") "0001"))
              (assert (= (apply-mask "1XX10" "000") "10010"))
              (assert (= (apply-mask "XXX1XXX0X" "11") "000100001"))
            )}
  apply-mask
  ([mask n]
   (let
      [pad-n (concat (repeat (- (count mask) (count n)) 0) n)
       rev-mask (reverse mask)
       nc (count n)]
      (assert (= (count pad-n) (count mask)))
     (str/join
       (map
         (fn [n m] (if (= m \X) n m))
         pad-n mask)))))
(test #'apply-mask)

(defn q1
  ([prog] (q1 prog {} ""))
  ([prog mem mask]
   (if (empty? prog)
     (let []
       mem
       (println (reduce + (map bin->int (vals mem)))))
     (let
       [line (first prog)]
       (cond
         (str/starts-with? line "mask") (recur (rest prog) mem (str/trim (second (str/split line #"="))))
         :else
          (let
            [[lhs rhs] (str/split line #" = ")
             memloc (Integer/parseInt (str/replace (str/replace lhs #"mem\[" "") #"\]" ""))
             n' (apply-mask mask (int->bin (Integer/parseInt rhs)))
             ]
            (recur (rest prog) (assoc mem memloc n') mask)
          )
        )
       ))))
(q1 lns)


(defn
  apply-mask2
  ([mask n]
   (let
      [pad-n (concat (repeat (- (count mask) (count n)) 0) n)
       rev-mask (reverse mask)
       nc (count n)]
      (assert (= (count pad-n) (count mask)))
     (str/join
       (map
         (fn [n m] (if (not= m \0) m n))
         pad-n mask)))))

(defn expand-addrs
  ([addr] (expand-addrs addr [""]))
  ([addr addrs]
   (if (empty? addr)
     addrs
     (let
       [c (first addr)]
       (cond
         (= c \X) (concat (expand-addrs (concat [0] (rest addr)) addrs)
                          (expand-addrs (concat [1] (rest addr)) addrs))
         :else (recur (rest addr) (map (fn [x] (str x c)) addrs)))))))
(test/testing
  (test/is (expand-addrs "X1101X")))

(defn q2
  ([prog] (q2 prog {} ""))
  ([prog mem mask]
   (if (empty? prog)
     (let []
       mem
       (println (reduce + (vals mem))))
     (let
       [line (first prog)]
       (cond
         (str/starts-with? line "mask")
            (recur (rest prog) mem (str/trim (second (str/split line #"="))))
         :else
          (let
            [[lhs rhs] (str/split line #" = ")
             memloc (int->bin (Integer/parseInt (str/replace (str/replace lhs #"mem\[" "") #"\]" "")))
             n' (Integer/parseInt rhs)
             addr (apply-mask2 mask memloc)
             ]
            (recur
              (rest prog)
              (reduce (fn [m x] (assoc m x n')) mem (expand-addrs addr))
              mask)
          )
        )
       ))))
(q2 lns)
