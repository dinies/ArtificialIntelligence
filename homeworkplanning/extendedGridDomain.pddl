(define (domain extended-grid)
  (:requirements :strips)
  (:predicates
    (conn ?square-1 ?square-2)
    (black ?square)
    (white ?square)
    (at ?who ?where )
    (place ?where ))
  (:action move
    :parameters (?who ?from ?to)
    :precondition (and (at ?who ?from)
                        (place ?from)
                        (place ?to)
                        (conn ?from ?to)
                        (white ?to))
    :effect (and (at ?who ?to)
              (not( at ?who ?from)))
    )
  (:action take-up
  :parameters (?who ?what ?from)
  :precondition (and (at ?who ?place)
                      (conn  ?place ?here )
                      (at ?what ?from)
                      (place ?from)
                      (place ?place)
                      (not (loaded ?who)))
  :effect (and (loaded ?who)
               (not(at ?what ?from)))
    )

  (:action put-down
  :parameters (?who ?what ?where)
  :precondition (and(loaded ?who)
                     ())
                  