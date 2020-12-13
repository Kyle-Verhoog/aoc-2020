(ns _ (:require [clojure.string :as str]))

(defn abs [x] (if (>= x 0) x (- x)))
(def lines (str/split-lines (slurp "twelve.txt")))

(defn rotate-cw [[x y :as v] ndeg]
  (if (= ndeg 0) v (rotate-cw [y (- x)] (- ndeg 90))))

(defn rotate-ccw [[x y :as v] ndeg] (rotate-cw v (- 360 ndeg)))

(defn q1 [{[i j :as d] :dir [x y :as p] :pos} line]
  (let* [dir (first line)
         n (Integer/parseInt (apply str (rest line)))]
    (case dir
      \N {:dir d :pos [x (+ y n)]}
      \S {:dir d :pos [x (- y n)]}
      \E {:dir d :pos [(+ x n) y]}
      \W {:dir d :pos [(- x n) y]}
      \F {:dir d :pos [(+ x (* n i)) (+ y (* n j))]}
      \R {:dir (rotate-cw d n) :pos p}
      \L {:dir (rotate-ccw d n) :pos p}
      )
    )
  )


(defn q2 [{[i j :as d] :dir [x y :as p] :pos} line]
  (let* [dir (first line)
         n (Integer/parseInt (apply str (rest line)))]
    (case dir
      \N {:dir [i (+ j n)] :pos p}
      \S {:dir [i (- j n)] :pos p}
      \E {:dir [(+ i n) j] :pos p}
      \W {:dir [(- i n) j] :pos p}
      \F {:dir d :pos [(+ x (* n i)) (+ y (* n j))]}
      \R {:dir (rotate-cw d n) :pos p}
      \L {:dir (rotate-ccw d n) :pos p}
      )
    )
  )


(println (reduce + (map abs (:pos (reduce q1 {:dir [1 0] :pos [0 0]} lines)))))
(println (reduce + (map abs (:pos (reduce q2 {:dir [10 1] :pos [0 0]} lines)))))
