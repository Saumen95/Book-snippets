counters = {
    'pupernickel': 2,
    'sourdough': 5
}

key = 'wheat'

if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1
