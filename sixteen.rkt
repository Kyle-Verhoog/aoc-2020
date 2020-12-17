#lang racket

(require racket/match)
(require racket/string)

(define lines (map string-trim (string-split (port->string (open-input-file "sixteen.txt")) "\n")))


;; part 1
(define p1-parse-rule
  (lambda (line s)
      (match
        (string-split line ":")
        [(list name rule)
         (let ([rngs (map (lambda (x) (list->set (stream->list (in-range (string->number (first x))
                                                              (add1 (string->number (second x)))))))
                          (map (lambda (x) (string-split x "-"))
                               (map string-trim (string-split rule "or"))))])
           (set-union s (first rngs) (second rngs))
           )])))
(define rules (foldl p1-parse-rule (set) (take lines (index-of lines ""))))
(define ticks (map (lambda (x) (map string->number (string-split x ","))) (list-tail lines (add1 (index-of lines "nearby tickets:")))))
; (println rules)
(println (foldl + 0 (flatten (map set->list (map (lambda (x) (set-subtract x rules)) (map list->set ticks))))))


;; part 2
(define myticket
  (map
    string->number
    (string-split
      (first (take (drop lines (add1 (index-of lines "your ticket:"))) 1)) ",")))
(define p2-parse-rule
  (lambda (line h)
      (match
        (string-split line ":")
        [(list field rule)
         (let ([rngs (map (lambda (x) (list->set (stream->list (in-range (string->number (first x))
                                                              (add1 (string->number (second x)))))))
                          (map (lambda (x) (string-split x "-"))
                               (map string-trim (string-split rule "or"))))])
           (hash-set h field (set-union (first rngs) (second rngs))))])))
(define p2rules (foldl p2-parse-rule (make-immutable-hash) (take lines (index-of lines ""))))
; (println p2rules)
(define valid-ticks (filter (lambda (x) (equal? (set-intersect rules (list->set x)) (list->set x))) ticks))
(define fields (hash-keys p2rules))
(define poss (map (lambda (x) (list->set fields)) fields))
; (println poss)
; (println valid-ticks)
(define res
  (foldl
    (lambda (line ps)
      (map
        (lambda (ps i)
          (foldl
            (lambda (f fs)
              (if (set-member? (hash-ref p2rules f) i) fs (set-remove fs f)))
            ps (set->list ps)))
        ps
        line)
      )
    poss
    valid-ticks))
;(println valid-ticks)
;(println fields)
;(println res)
(define reduce
  (lambda (posfields)
    (let* ([resolved (foldl set-union (set) (filter (lambda (x) (= (set-count x) 1)) posfields))])
      (if (= (set-count resolved) (length posfields))
        posfields
        (reduce (map (lambda (x) (if (> (set-count x) 1) (set-subtract x resolved) x)) posfields))))))

(define res-fields (map (lambda (x) (first (set->list x))) (reduce res)))
; (println res-fields)
; (println myticket)
; (println (map (lambda (field v) (if (string=? (first (string-split field)) "departure") v 1)) res-fields myticket))
(println
  (foldl * 1 (map (lambda (field v) (if (string=? (first (string-split field " ")) "departure") v 1)) res-fields myticket)))
