(define (over-or-under num1 num2) 
        ; (cond 
        ;   ((< num1 num2) -1)
        ;   ((= num1 num2) 0)
        ;   (else 1)
        ; )

        (if (< num1 num2) -1 
        (if (= num1 num2) 0 1)
        )
)

(define (make-adder num) 
        (lambda (inc) (+ inc num))
)

(define (composed f g) 
        (lambda (x) (f (g x))) 
)

(define (repeat f n) 
        (lambda (x) 
          (if 
            (= n 1) (f x)
            ((repeat f (- n 1)) (f x))
          )
        )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))


(define (gcd a b) 
        (if 
          (> b a) (gcd b a)
          (cond  
            ((zero? (modulo a b)) b)
            (else (gcd b (modulo a b)))
          )
        )
)
