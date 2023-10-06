(define (square n) (* n n))

(define (pow base exp) 
        (if (= 1 exp)
            base 
            (if 
              (zero? (modulo exp 2))
              (square (pow base (/ exp 2)))
              (* base (square (pow base (/ (- exp 1) 2))))
            )
        )
)

; let的绑定:  (在一个表达式领域内)
; let 和 lambda
(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

; 问题出在哪,  研究一下 |  执行过程的问题 | 如何加入知识体系中
; 嵌套表达式的执行过程 | 执行的先后顺序
(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))
