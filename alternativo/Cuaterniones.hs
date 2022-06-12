{-# OPTIONS_GHC -Wno-missing-methods #-}

-- Se define los elementos del modulo que se exportan
module Cuaterniones( Cuaternion ( Cuaternion ) ) where

-- Se define el tipo Cuaternion
data Cuaternion =
  Cuaternion Integer Integer Integer Integer
  deriving (Show, Eq)

-- Modificamos la instancia `Num` para
instance Num Cuaternion where
  -- Suma entre cuaterniones
  (Cuaternion a b c d) + (Cuaternion a' b' c' d') =
    Cuaternion (a + a') (b + b') (c + c') (d + d')

  (Cuaternion a b c d) * (Cuaternion a' b' c' d') =
    Cuaternion (a * a' - b * b' - c * c' - d * d')
              (a * b' + b * a' + c * d' - d * c')
              (a * c' + c * a' + d * b' - b * d')
              (a * d' + d * a' + b * c' - c * b')

  -- Negacion de un cuaternion, se usa con el operador (-)
  negate (Cuaternion a b c d) =
    Cuaternion a (negate b) (negate c) (negate d)

  -- Construccion de un cuaternion desde un entero, para operaciones con escalares
  fromInteger i = Cuaternion (fromInteger i) 0 0 0
