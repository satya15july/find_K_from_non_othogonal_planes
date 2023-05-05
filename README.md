# Introduction
This project is about finding Camera Callibration(K) from 3 pair of vanishing points which are not orthogonal.

![input](https://user-images.githubusercontent.com/22910010/236415739-91cea340-3cad-478d-8f8d-22237e08aeba.png)

# How to Use

## Annotate Image
Annotate the input image by running `python3 main.py` and then select the 3 pairs of orthogonal vanishing points.This will generate 'final_cord.npy'.

![image_anotated](https://user-images.githubusercontent.com/22910010/236415830-2a28cdc0-e53d-409f-972b-eb8ef9437346.png)

You can skip this step and directly procede to run the program as 'final_cord.npy' which is already present.

# Output

```
K: [[1100.8404837942396, 0, 503.3137644929781],
    [0, 1100.8404837942396, 306.56805767470127],
    [0, 0, 1]]

Angele between first_plane and second_plane : 63.134822064695776
Angele between first_plane and third_plane : 85.25810291007781
Angele between second_plane and third_plane : 85.13401960546055

```

# Conclusion

