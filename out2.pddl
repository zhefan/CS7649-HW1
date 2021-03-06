(define (problem sokoban)
  (:domain sokoban-domain)
  (:objects c01 c02 c10 c11 c12 c20 c22)
  (:init 
         (not (hasAgent c01) ) (not (hasBlock c01) )
         (not (hasAgent c02) ) (not (hasBlock c02) )
              (hasAgent c10)   (not (hasBlock c10) )
         (not (hasAgent c11) )      (hasBlock c11)
         (not (hasAgent c12) ) (not (hasBlock c12) )
         (not (hasAgent c20) ) (not (hasBlock c20) )
         (not (hasAgent c22) ) (not (hasBlock c22) )
         (adj c01 c11) (adj c11 c01)
         (adj c01 c02) (adj c02 c01)
         (adj c02 c12) (adj c12 c02)
         (adj c10 c20) (adj c20 c10)
         (adj c10 c11) (adj c11 c10)
         (adj c11 c12) (adj c12 c11)
         (adj c12 c22) (adj c22 c12)
         (collinear c02 c12 c22) (collinear c22 c12 c02)
         (collinear c10 c11 c12) (collinear c12 c11 c10)
  )
  (:goal (hasBlock c22))
)
