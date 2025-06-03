def mix_args(*args, **kwargs):
	print("Positional:", args)
	print("Keyword:", kwargs)

mix_args(1, 2, 3, name="Suresh", job="SDET", city="Bangalore", country="India")
