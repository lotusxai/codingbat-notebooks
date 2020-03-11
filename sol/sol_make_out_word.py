def make_out_word(out, word):
  l = len(out)
  l = l/2
  return out[:l] + word + out[l:]
