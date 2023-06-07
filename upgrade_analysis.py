import json

def optimize_engine(low=True,mid=True,high=True):
	if low:
		print('Low-cost engine upgrades')
	if mid:
		print('Mid-priced engine upgrades')
	if high:
		print('High-end engine upgrades')
def optimize_suspension(low=True,mid=True,high=True):
	if low:
		print('Low-cost suspension upgrades')
	if mid:
		print('Mid-priced suspension upgrades')
	if high:
		print('High-end suspension upgrades')
def optimize_exhaust(low=True,mid=True,high=True):
	if low:
		print('Low-cost exhaust '+
					'upgrades')
	if mid:
		print('Mid-priced exhaust upgrades')
	if high:
		print('High-end exhaust upgrades')
def optimize_all(low=True,mid=True,high=True):
	optimize_engine(low=low,mid=mid,high=high)
	optimize_suspension(low=low,mid=mid,high=high)
	optimize_exhaust(low=low,mid=mid,high=high)



