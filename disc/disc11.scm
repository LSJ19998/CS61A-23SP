(define (vir-fib n)
    (cond 
        ((= 1 n) 1)
        ((= 0 n) 0)
        (else (+ (vir-fib (- n 1)) (vir-fib (- n 2)))) 
    )
)


(define with-list (list (list 'a (list 'b)) (list 'c 'd (list (list 'e)))))