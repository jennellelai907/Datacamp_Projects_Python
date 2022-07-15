no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna())
plt.ylabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

no_bands = no_bands.sort_values('num_songs', ascending=False)

display(no_bands.head(15))
