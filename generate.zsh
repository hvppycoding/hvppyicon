#!/bin/zsh

for letter in {A..Z}; do
  hvppyicon -bg "rgba(255, 255, 255, 255)" -fc "rgba(0, 0, 0, 255)" -o "doc/images/${letter}_white.png" $letter
done

for letter in {A..Z}; do
  echo "![${letter}_white.png](doc/images/${letter}_white.png)"
done