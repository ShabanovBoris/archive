f :: Double -> Double -> Double -> Double -> Double
f a b c d  = sqrt ((b-a)^2+(d-c)^2)
n :: (Double,Double) -> (Double,Double) -> (Double,Double) -> (Double,Double) -> String
n (x1,y1) (x2,y2) (x3,y3) (x4,y4) = if (f x1 x2 y1 y2 == f x2 x3 y2 y3) && (f x2 x3 y2 y3 == f x3 x4 y3 y4) && (f x3 x4 y3 y4 == f x4 x1 y4 y1) && (f x1 x3 y1 y3 == f x2 x4 y2 y4) then "Yes" else "No"
        