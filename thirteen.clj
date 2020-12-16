(ns _ (:require [clojure.string :as str]))

(defn abs [x] (if (>= x 0) x (- x)))
(defn gcd [x y] (if (zero? y) x (recur y (mod x y))))
(def ts
  (filter
    (fn [x] (not= (second x) "x"))
    (map-indexed
      (fn [i x] [i (if (not= x "x") (bigint x) x)])
      (str/split (second (str/split-lines (slurp "thirteen.txt"))) #","))))


(println ts)
(def coprimes
  (let [nums (map second ts)]
    (map
      (fn [x]
        (map
          (fn [y] (if (not= x y) (gcd x y) 1))
          nums))
      nums)))

(defn eea
  ([a b]
   (let [r (eea [a b] [1 0] [0 1])]
         r))
  ([[r0 r1] [s0 s1] [t0 t1]]
   (if (= r1 0) [r0 s0 t0]
     (let [q (quot r0 r1)
           r0' r1
           r1' (- r0 (* q r1))
           s0' s1
           s1' (- s0 (* q s1))
           t0' t1
           t1' (- t0 (* q t1))]
       (eea [r0' r1'] [s0' s1'] [t0' t1'])))))
(println (eea 240 46))

(defn ngcd
  ([nums] (ngcd (first nums) (rest nums)))
  ([_gcd nums]
   (if (empty? nums) _gcd (ngcd (gcd _gcd (first nums)) (rest nums)))))


(defn pt2
  ([ans]
   (println ans)
   (if (= (count ans) 1)
     (let [[a n] (first ans)]
       [a n])
     (let
       [[a1 n1] (first ans)
        [a2 n2] (second ans)
        [gcd m1 m2] (eea n1 n2)
        n' (* n1 n2)]
       (pt2 (concat [[(+ (* a1 m2 n2) (* a2 m1 n1)) n']] (rest (rest ans))))))))

(let [[a n] (pt2 (map (fn [[a n]] [(- a) n]) ts))]
  (println (mod a n)))
