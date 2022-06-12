{-# LANGUAGE InstanceSigs #-}
{-# LANGUAGE UnicodeSyntax #-}

data Cuaternion =
  Cuaternion Integer Integer Integer Integer
  deriving (Show, Eq)

instance Num Cuaternion where
  (Cuaternion a b c d) + (Cuaternion a' b' c' d') =
    Cuaternion (a + a') (b + b') (c + c') (d + d')

  (*) :: Cuaternion -> Cuaternion -> Cuaternion
  (Cuaternion a b c d) * (Cuaternion a' b' c' d') =
    Cuaternion (a * a' - b * b' - c * c' - d * d')
               (a * b' + b * a' + c * d' - d * c')
               (a * c' + c * a' + d * b' - b * d')
               (a * d' + d * a' + b * c' - c * b')

  -- (*) :: Cuaternion -> Num -> Cuaternion
  -- (Cuaternion a b c d) * n = Cuaternion (a * n) (b * n) (c * n) (d * n)

  

  negate (Cuaternion a b c d) =
    Cuaternion a (negate b) (negate c) (negate d)

  -- abs :: Cuaternion -> Float
  -- abs (Cuaternion a b c d) = (fromIntegral (a^2 + b ^2 + c ^2 + d ^2))

  fromInteger i = Cuaternion (fromInteger i) 0 0 0


-- (*) :: Cuaternion -> Integer -> Cuaternion
-- (Cuaternion a b c d) * n = Cuaternion (a * n) (b * n) (c * n) (d * n)

  

-- (~) :: Cuaternion -> Cuaternion
-- (~) _ (Cuaternion a b c d) = negate (Cuaternion a b c d)

