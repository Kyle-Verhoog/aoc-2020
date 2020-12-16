(import collections)

;(setv l (list (map int (-> "fifteen.txt" open .readlines (get 0) .strip (.split ",")))))
(setv l [20 0 1 11 6 3])
; (setv l [0 3 6])
; (setv l [2 1 3])
; (setv l [3 1 2])

; (setv N 2020)
(setv N 30000000)

(defn pt1 [t n]
  (do
    (setv d (get t 0))
    (setv mostrec (get t 1))
    (setv mostrec_vs (get d mostrec))
    (if (= (len mostrec_vs) 1)
      (do
        ; If the most recent number has only been spoken
        ; once, say 0.
        (.append (get d 0) n)
        (if (= n N) 0 (, d 0)))
      (do
        (setv next (- (get mostrec_vs -1) (get mostrec_vs -2)))
        (.append (get d next) n)
        ; (print n "speaking" next)
        (if (= n N) next (, d next))
        ))
      ))

(setv d
  (reduce
    (fn [d x]
    (do
      (setv turn (+ 1 (get x 0)))
      (setv n (get x 1))
      (.append (get d n) turn)
      d))
    (enumerate l)
    (collections.defaultdict (fn [] (collections.deque [] 2)))))
(print d)
(print (reduce pt1 (range (-> l len (+ 1)) (+ N 1)) (, d (get l -1))))
