from .table import TableRow

class SchemaMigrationsRow(TableRow):
	def __init__(self):
		super().__init__('schema_migrations')
		self._version = None
		self._dirty = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def version(self):
		return self._version

	@version.setter
	def version(self, version):
		self._version = version

	@property
	def dirty(self):
		return self._dirty

	@dirty.setter
	def dirty(self, dirty):
		self._dirty = dirty

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.version, self.dirty]
		else:
			return [self.version, self.dirty]

class TagsRow(TableRow):
	def __init__(self):
		super().__init__('tags')
		self._id = None
		self._name = None
		self._created_at = None
		self._updated_at = None
		self._ignore_auto_tag = None
		self._description = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	@property
	def ignore_auto_tag(self):
		return self._ignore_auto_tag

	@ignore_auto_tag.setter
	def ignore_auto_tag(self, ignore_auto_tag):
		self._ignore_auto_tag = ignore_auto_tag

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, description):
		self._description = description

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.name, self.created_at, self.updated_at, self.ignore_auto_tag, self.description]
		else:
			return [self.name, self.created_at, self.updated_at, self.ignore_auto_tag, self.description]

class SqliteSequenceRow(TableRow):
	def __init__(self):
		super().__init__('sqlite_sequence')
		self._name = None
		self._seq = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def seq(self):
		return self._seq

	@seq.setter
	def seq(self, seq):
		self._seq = seq

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.name, self.seq]
		else:
			return [self.name, self.seq]

class StudiosRow(TableRow):
	def __init__(self):
		super().__init__('studios')
		self._id = None
		self._checksum = None
		self._name = None
		self._url = None
		self._parent_id = None
		self._created_at = None
		self._updated_at = None
		self._details = None
		self._rating = None
		self._ignore_auto_tag = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def parent_id(self):
		return self._parent_id

	@parent_id.setter
	def parent_id(self, parent_id):
		self._parent_id = parent_id

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, details):
		self._details = details

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def ignore_auto_tag(self):
		return self._ignore_auto_tag

	@ignore_auto_tag.setter
	def ignore_auto_tag(self, ignore_auto_tag):
		self._ignore_auto_tag = ignore_auto_tag

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.checksum, self.name, self.url, self.parent_id, self.created_at, self.updated_at, self.details, self.rating, self.ignore_auto_tag]
		else:
			return [self.checksum, self.name, self.url, self.parent_id, self.created_at, self.updated_at, self.details, self.rating, self.ignore_auto_tag]

class PerformersRow(TableRow):
	def __init__(self):
		super().__init__('performers')
		self._id = None
		self._checksum = None
		self._name = None
		self._gender = None
		self._url = None
		self._twitter = None
		self._instagram = None
		self._birthdate = None
		self._ethnicity = None
		self._country = None
		self._eye_color = None
		self._height = None
		self._measurements = None
		self._fake_tits = None
		self._career_length = None
		self._tattoos = None
		self._piercings = None
		self._aliases = None
		self._favorite = None
		self._created_at = None
		self._updated_at = None
		self._details = None
		self._death_date = None
		self._hair_color = None
		self._weight = None
		self._rating = None
		self._ignore_auto_tag = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def gender(self):
		return self._gender

	@gender.setter
	def gender(self, gender):
		self._gender = gender

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def twitter(self):
		return self._twitter

	@twitter.setter
	def twitter(self, twitter):
		self._twitter = twitter

	@property
	def instagram(self):
		return self._instagram

	@instagram.setter
	def instagram(self, instagram):
		self._instagram = instagram

	@property
	def birthdate(self):
		return self._birthdate

	@birthdate.setter
	def birthdate(self, birthdate):
		self._birthdate = birthdate

	@property
	def ethnicity(self):
		return self._ethnicity

	@ethnicity.setter
	def ethnicity(self, ethnicity):
		self._ethnicity = ethnicity

	@property
	def country(self):
		return self._country

	@country.setter
	def country(self, country):
		self._country = country

	@property
	def eye_color(self):
		return self._eye_color

	@eye_color.setter
	def eye_color(self, eye_color):
		self._eye_color = eye_color

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height

	@property
	def measurements(self):
		return self._measurements

	@measurements.setter
	def measurements(self, measurements):
		self._measurements = measurements

	@property
	def fake_tits(self):
		return self._fake_tits

	@fake_tits.setter
	def fake_tits(self, fake_tits):
		self._fake_tits = fake_tits

	@property
	def career_length(self):
		return self._career_length

	@career_length.setter
	def career_length(self, career_length):
		self._career_length = career_length

	@property
	def tattoos(self):
		return self._tattoos

	@tattoos.setter
	def tattoos(self, tattoos):
		self._tattoos = tattoos

	@property
	def piercings(self):
		return self._piercings

	@piercings.setter
	def piercings(self, piercings):
		self._piercings = piercings

	@property
	def aliases(self):
		return self._aliases

	@aliases.setter
	def aliases(self, aliases):
		self._aliases = aliases

	@property
	def favorite(self):
		return self._favorite

	@favorite.setter
	def favorite(self, favorite):
		self._favorite = favorite

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, details):
		self._details = details

	@property
	def death_date(self):
		return self._death_date

	@death_date.setter
	def death_date(self, death_date):
		self._death_date = death_date

	@property
	def hair_color(self):
		return self._hair_color

	@hair_color.setter
	def hair_color(self, hair_color):
		self._hair_color = hair_color

	@property
	def weight(self):
		return self._weight

	@weight.setter
	def weight(self, weight):
		self._weight = weight

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def ignore_auto_tag(self):
		return self._ignore_auto_tag

	@ignore_auto_tag.setter
	def ignore_auto_tag(self, ignore_auto_tag):
		self._ignore_auto_tag = ignore_auto_tag

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.checksum, self.name, self.gender, self.url, self.twitter, self.instagram, self.birthdate, self.ethnicity, self.country, self.eye_color, self.height, self.measurements, self.fake_tits, self.career_length, self.tattoos, self.piercings, self.aliases, self.favorite, self.created_at, self.updated_at, self.details, self.death_date, self.hair_color, self.weight, self.rating, self.ignore_auto_tag]
		else:
			return [self.checksum, self.name, self.gender, self.url, self.twitter, self.instagram, self.birthdate, self.ethnicity, self.country, self.eye_color, self.height, self.measurements, self.fake_tits, self.career_length, self.tattoos, self.piercings, self.aliases, self.favorite, self.created_at, self.updated_at, self.details, self.death_date, self.hair_color, self.weight, self.rating, self.ignore_auto_tag]

class MoviesRow(TableRow):
	def __init__(self):
		super().__init__('movies')
		self._id = None
		self._name = None
		self._aliases = None
		self._duration = None
		self._date = None
		self._rating = None
		self._studio_id = None
		self._director = None
		self._synopsis = None
		self._checksum = None
		self._url = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def aliases(self):
		return self._aliases

	@aliases.setter
	def aliases(self, aliases):
		self._aliases = aliases

	@property
	def duration(self):
		return self._duration

	@duration.setter
	def duration(self, duration):
		self._duration = duration

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		self._date = date

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def director(self):
		return self._director

	@director.setter
	def director(self, director):
		self._director = director

	@property
	def synopsis(self):
		return self._synopsis

	@synopsis.setter
	def synopsis(self, synopsis):
		self._synopsis = synopsis

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.name, self.aliases, self.duration, self.date, self.rating, self.studio_id, self.director, self.synopsis, self.checksum, self.url, self.created_at, self.updated_at]
		else:
			return [self.name, self.aliases, self.duration, self.date, self.rating, self.studio_id, self.director, self.synopsis, self.checksum, self.url, self.created_at, self.updated_at]

class ScrapedItemsRow(TableRow):
	def __init__(self):
		super().__init__('scraped_items')
		self._id = None
		self._title = None
		self._description = None
		self._url = None
		self._date = None
		self._rating = None
		self._tags = None
		self._models = None
		self._episode = None
		self._gallery_filename = None
		self._gallery_url = None
		self._video_filename = None
		self._video_url = None
		self._studio_id = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, description):
		self._description = description

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		self._date = date

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def tags(self):
		return self._tags

	@tags.setter
	def tags(self, tags):
		self._tags = tags

	@property
	def models(self):
		return self._models

	@models.setter
	def models(self, models):
		self._models = models

	@property
	def episode(self):
		return self._episode

	@episode.setter
	def episode(self, episode):
		self._episode = episode

	@property
	def gallery_filename(self):
		return self._gallery_filename

	@gallery_filename.setter
	def gallery_filename(self, gallery_filename):
		self._gallery_filename = gallery_filename

	@property
	def gallery_url(self):
		return self._gallery_url

	@gallery_url.setter
	def gallery_url(self, gallery_url):
		self._gallery_url = gallery_url

	@property
	def video_filename(self):
		return self._video_filename

	@video_filename.setter
	def video_filename(self, video_filename):
		self._video_filename = video_filename

	@property
	def video_url(self):
		return self._video_url

	@video_url.setter
	def video_url(self, video_url):
		self._video_url = video_url

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.title, self.description, self.url, self.date, self.rating, self.tags, self.models, self.episode, self.gallery_filename, self.gallery_url, self.video_filename, self.video_url, self.studio_id, self.created_at, self.updated_at]
		else:
			return [self.title, self.description, self.url, self.date, self.rating, self.tags, self.models, self.episode, self.gallery_filename, self.gallery_url, self.video_filename, self.video_url, self.studio_id, self.created_at, self.updated_at]

class SceneMarkersRow(TableRow):
	def __init__(self):
		super().__init__('scene_markers')
		self._id = None
		self._title = None
		self._seconds = None
		self._primary_tag_id = None
		self._scene_id = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def seconds(self):
		return self._seconds

	@seconds.setter
	def seconds(self, seconds):
		self._seconds = seconds

	@property
	def primary_tag_id(self):
		return self._primary_tag_id

	@primary_tag_id.setter
	def primary_tag_id(self, primary_tag_id):
		self._primary_tag_id = primary_tag_id

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.title, self.seconds, self.primary_tag_id, self.scene_id, self.created_at, self.updated_at]
		else:
			return [self.title, self.seconds, self.primary_tag_id, self.scene_id, self.created_at, self.updated_at]

class PerformerStashIdsRow(TableRow):
	def __init__(self):
		super().__init__('performer_stash_ids')
		self._performer_id = None
		self._endpoint = None
		self._stash_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def endpoint(self):
		return self._endpoint

	@endpoint.setter
	def endpoint(self, endpoint):
		self._endpoint = endpoint

	@property
	def stash_id(self):
		return self._stash_id

	@stash_id.setter
	def stash_id(self, stash_id):
		self._stash_id = stash_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.endpoint, self.stash_id]
		else:
			return [self.performer_id, self.endpoint, self.stash_id]

class StudioStashIdsRow(TableRow):
	def __init__(self):
		super().__init__('studio_stash_ids')
		self._studio_id = None
		self._endpoint = None
		self._stash_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def endpoint(self):
		return self._endpoint

	@endpoint.setter
	def endpoint(self, endpoint):
		self._endpoint = endpoint

	@property
	def stash_id(self):
		return self._stash_id

	@stash_id.setter
	def stash_id(self, stash_id):
		self._stash_id = stash_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.studio_id, self.endpoint, self.stash_id]
		else:
			return [self.studio_id, self.endpoint, self.stash_id]

class SavedFiltersRow(TableRow):
	def __init__(self):
		super().__init__('saved_filters')
		self._id = None
		self._name = None
		self._mode = None
		self._filter = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def mode(self):
		return self._mode

	@mode.setter
	def mode(self, mode):
		self._mode = mode

	@property
	def filter(self):
		return self._filter

	@filter.setter
	def filter(self, filter):
		self._filter = filter

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.name, self.mode, self.filter]
		else:
			return [self.name, self.mode, self.filter]

class TagsRelationsRow(TableRow):
	def __init__(self):
		super().__init__('tags_relations')
		self._parent_id = None
		self._child_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def parent_id(self):
		return self._parent_id

	@parent_id.setter
	def parent_id(self, parent_id):
		self._parent_id = parent_id

	@property
	def child_id(self):
		return self._child_id

	@child_id.setter
	def child_id(self, child_id):
		self._child_id = child_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.parent_id, self.child_id]
		else:
			return [self.parent_id, self.child_id]

class FoldersRow(TableRow):
	def __init__(self):
		super().__init__('folders')
		self._id = None
		self._path = None
		self._parent_folder_id = None
		self._mod_time = None
		self._created_at = None
		self._updated_at = None
		self._zip_file_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def parent_folder_id(self):
		return self._parent_folder_id

	@parent_folder_id.setter
	def parent_folder_id(self, parent_folder_id):
		self._parent_folder_id = parent_folder_id

	@property
	def mod_time(self):
		return self._mod_time

	@mod_time.setter
	def mod_time(self, mod_time):
		self._mod_time = mod_time

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	@property
	def zip_file_id(self):
		return self._zip_file_id

	@zip_file_id.setter
	def zip_file_id(self, zip_file_id):
		self._zip_file_id = zip_file_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.path, self.parent_folder_id, self.mod_time, self.created_at, self.updated_at, self.zip_file_id]
		else:
			return [self.path, self.parent_folder_id, self.mod_time, self.created_at, self.updated_at, self.zip_file_id]

class FilesRow(TableRow):
	def __init__(self):
		super().__init__('files')
		self._id = None
		self._basename = None
		self._zip_file_id = None
		self._parent_folder_id = None
		self._size = None
		self._mod_time = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def basename(self):
		return self._basename

	@basename.setter
	def basename(self, basename):
		self._basename = basename

	@property
	def zip_file_id(self):
		return self._zip_file_id

	@zip_file_id.setter
	def zip_file_id(self, zip_file_id):
		self._zip_file_id = zip_file_id

	@property
	def parent_folder_id(self):
		return self._parent_folder_id

	@parent_folder_id.setter
	def parent_folder_id(self, parent_folder_id):
		self._parent_folder_id = parent_folder_id

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, size):
		self._size = size

	@property
	def mod_time(self):
		return self._mod_time

	@mod_time.setter
	def mod_time(self, mod_time):
		self._mod_time = mod_time

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.basename, self.zip_file_id, self.parent_folder_id, self.size, self.mod_time, self.created_at, self.updated_at]
		else:
			return [self.basename, self.zip_file_id, self.parent_folder_id, self.size, self.mod_time, self.created_at, self.updated_at]

class FilesFingerprintsRow(TableRow):
	def __init__(self):
		super().__init__('files_fingerprints')
		self._file_id = None
		self._type = None
		self._fingerprint = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def file_id(self):
		return self._file_id

	@file_id.setter
	def file_id(self, file_id):
		self._file_id = file_id

	@property
	def type(self):
		return self._type

	@type.setter
	def type(self, type):
		self._type = type

	@property
	def fingerprint(self):
		return self._fingerprint

	@fingerprint.setter
	def fingerprint(self, fingerprint):
		self._fingerprint = fingerprint

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.file_id, self.type, self.fingerprint]
		else:
			return [self.file_id, self.type, self.fingerprint]

class VideoFilesRow(TableRow):
	def __init__(self):
		super().__init__('video_files')
		self._file_id = None
		self._duration = None
		self._video_codec = None
		self._format = None
		self._audio_codec = None
		self._width = None
		self._height = None
		self._frame_rate = None
		self._bit_rate = None
		self._interactive = None
		self._interactive_speed = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def file_id(self):
		return self._file_id

	@file_id.setter
	def file_id(self, file_id):
		self._file_id = file_id

	@property
	def duration(self):
		return self._duration

	@duration.setter
	def duration(self, duration):
		self._duration = duration

	@property
	def video_codec(self):
		return self._video_codec

	@video_codec.setter
	def video_codec(self, video_codec):
		self._video_codec = video_codec

	@property
	def format(self):
		return self._format

	@format.setter
	def format(self, format):
		self._format = format

	@property
	def audio_codec(self):
		return self._audio_codec

	@audio_codec.setter
	def audio_codec(self, audio_codec):
		self._audio_codec = audio_codec

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height

	@property
	def frame_rate(self):
		return self._frame_rate

	@frame_rate.setter
	def frame_rate(self, frame_rate):
		self._frame_rate = frame_rate

	@property
	def bit_rate(self):
		return self._bit_rate

	@bit_rate.setter
	def bit_rate(self, bit_rate):
		self._bit_rate = bit_rate

	@property
	def interactive(self):
		return self._interactive

	@interactive.setter
	def interactive(self, interactive):
		self._interactive = interactive

	@property
	def interactive_speed(self):
		return self._interactive_speed

	@interactive_speed.setter
	def interactive_speed(self, interactive_speed):
		self._interactive_speed = interactive_speed

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.file_id, self.duration, self.video_codec, self.format, self.audio_codec, self.width, self.height, self.frame_rate, self.bit_rate, self.interactive, self.interactive_speed]
		else:
			return [self.file_id, self.duration, self.video_codec, self.format, self.audio_codec, self.width, self.height, self.frame_rate, self.bit_rate, self.interactive, self.interactive_speed]

class VideoCaptionsRow(TableRow):
	def __init__(self):
		super().__init__('video_captions')
		self._file_id = None
		self._language_code = None
		self._filename = None
		self._caption_type = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def file_id(self):
		return self._file_id

	@file_id.setter
	def file_id(self, file_id):
		self._file_id = file_id

	@property
	def language_code(self):
		return self._language_code

	@language_code.setter
	def language_code(self, language_code):
		self._language_code = language_code

	@property
	def filename(self):
		return self._filename

	@filename.setter
	def filename(self, filename):
		self._filename = filename

	@property
	def caption_type(self):
		return self._caption_type

	@caption_type.setter
	def caption_type(self, caption_type):
		self._caption_type = caption_type

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.file_id, self.language_code, self.filename, self.caption_type]
		else:
			return [self.file_id, self.language_code, self.filename, self.caption_type]

class ImageFilesRow(TableRow):
	def __init__(self):
		super().__init__('image_files')
		self._file_id = None
		self._format = None
		self._width = None
		self._height = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def file_id(self):
		return self._file_id

	@file_id.setter
	def file_id(self, file_id):
		self._file_id = file_id

	@property
	def format(self):
		return self._format

	@format.setter
	def format(self, format):
		self._format = format

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.file_id, self.format, self.width, self.height]
		else:
			return [self.file_id, self.format, self.width, self.height]

class ImagesFilesRow(TableRow):
	def __init__(self):
		super().__init__('images_files')
		self._image_id = None
		self._file_id = None
		self._primary = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def image_id(self):
		return self._image_id

	@image_id.setter
	def image_id(self, image_id):
		self._image_id = image_id

	@property
	def file_id(self):
		return self._file_id

	@file_id.setter
	def file_id(self, file_id):
		self._file_id = file_id

	@property
	def primary(self):
		return self._primary

	@primary.setter
	def primary(self, primary):
		self._primary = primary

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.image_id, self.file_id, self.primary]
		else:
			return [self.image_id, self.file_id, self.primary]

class GalleriesFilesRow(TableRow):
	def __init__(self):
		super().__init__('galleries_files')
		self._gallery_id = None
		self._file_id = None
		self._primary = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	@property
	def file_id(self):
		return self._file_id

	@file_id.setter
	def file_id(self, file_id):
		self._file_id = file_id

	@property
	def primary(self):
		return self._primary

	@primary.setter
	def primary(self, primary):
		self._primary = primary

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.gallery_id, self.file_id, self.primary]
		else:
			return [self.gallery_id, self.file_id, self.primary]

class ScenesFilesRow(TableRow):
	def __init__(self):
		super().__init__('scenes_files')
		self._scene_id = None
		self._file_id = None
		self._primary = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def file_id(self):
		return self._file_id

	@file_id.setter
	def file_id(self, file_id):
		self._file_id = file_id

	@property
	def primary(self):
		return self._primary

	@primary.setter
	def primary(self, primary):
		self._primary = primary

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.file_id, self.primary]
		else:
			return [self.scene_id, self.file_id, self.primary]

class ImagesRow(TableRow):
	def __init__(self):
		super().__init__('images')
		self._id = None
		self._title = None
		self._rating = None
		self._studio_id = None
		self._o_counter = None
		self._organized = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def o_counter(self):
		return self._o_counter

	@o_counter.setter
	def o_counter(self, o_counter):
		self._o_counter = o_counter

	@property
	def organized(self):
		return self._organized

	@organized.setter
	def organized(self, organized):
		self._organized = organized

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.title, self.rating, self.studio_id, self.o_counter, self.organized, self.created_at, self.updated_at]
		else:
			return [self.title, self.rating, self.studio_id, self.o_counter, self.organized, self.created_at, self.updated_at]

class GalleriesRow(TableRow):
	def __init__(self):
		super().__init__('galleries')
		self._id = None
		self._folder_id = None
		self._title = None
		self._url = None
		self._date = None
		self._details = None
		self._studio_id = None
		self._rating = None
		self._organized = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def folder_id(self):
		return self._folder_id

	@folder_id.setter
	def folder_id(self, folder_id):
		self._folder_id = folder_id

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		self._date = date

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, details):
		self._details = details

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def organized(self):
		return self._organized

	@organized.setter
	def organized(self, organized):
		self._organized = organized

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.folder_id, self.title, self.url, self.date, self.details, self.studio_id, self.rating, self.organized, self.created_at, self.updated_at]
		else:
			return [self.folder_id, self.title, self.url, self.date, self.details, self.studio_id, self.rating, self.organized, self.created_at, self.updated_at]

class ScenesRow(TableRow):
	def __init__(self):
		super().__init__('scenes')
		self._id = None
		self._title = None
		self._details = None
		self._url = None
		self._date = None
		self._rating = None
		self._studio_id = None
		self._o_counter = None
		self._organized = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, details):
		self._details = details

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		self._date = date

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def o_counter(self):
		return self._o_counter

	@o_counter.setter
	def o_counter(self, o_counter):
		self._o_counter = o_counter

	@property
	def organized(self):
		return self._organized

	@organized.setter
	def organized(self, organized):
		self._organized = organized

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.title, self.details, self.url, self.date, self.rating, self.studio_id, self.o_counter, self.organized, self.created_at, self.updated_at]
		else:
			return [self.title, self.details, self.url, self.date, self.rating, self.studio_id, self.o_counter, self.organized, self.created_at, self.updated_at]

class PerformersImageRow(TableRow):
	def __init__(self):
		super().__init__('performers_image')
		self._performer_id = None
		self._image = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, image):
		self._image = image

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.image]
		else:
			return [self.performer_id, self.image]

class StudiosImageRow(TableRow):
	def __init__(self):
		super().__init__('studios_image')
		self._studio_id = None
		self._image = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, image):
		self._image = image

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.studio_id, self.image]
		else:
			return [self.studio_id, self.image]

class MoviesImagesRow(TableRow):
	def __init__(self):
		super().__init__('movies_images')
		self._movie_id = None
		self._front_image = None
		self._back_image = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def movie_id(self):
		return self._movie_id

	@movie_id.setter
	def movie_id(self, movie_id):
		self._movie_id = movie_id

	@property
	def front_image(self):
		return self._front_image

	@front_image.setter
	def front_image(self, front_image):
		self._front_image = front_image

	@property
	def back_image(self):
		return self._back_image

	@back_image.setter
	def back_image(self, back_image):
		self._back_image = back_image

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.movie_id, self.front_image, self.back_image]
		else:
			return [self.movie_id, self.front_image, self.back_image]

class TagsImageRow(TableRow):
	def __init__(self):
		super().__init__('tags_image')
		self._tag_id = None
		self._image = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, image):
		self._image = image

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.tag_id, self.image]
		else:
			return [self.tag_id, self.image]

class PerformersScenesRow(TableRow):
	def __init__(self):
		super().__init__('performers_scenes')
		self._performer_id = None
		self._scene_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.scene_id]
		else:
			return [self.performer_id, self.scene_id]

class SceneMarkersTagsRow(TableRow):
	def __init__(self):
		super().__init__('scene_markers_tags')
		self._scene_marker_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_marker_id(self):
		return self._scene_marker_id

	@scene_marker_id.setter
	def scene_marker_id(self, scene_marker_id):
		self._scene_marker_id = scene_marker_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_marker_id, self.tag_id]
		else:
			return [self.scene_marker_id, self.tag_id]

class ScenesTagsRow(TableRow):
	def __init__(self):
		super().__init__('scenes_tags')
		self._scene_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.tag_id]
		else:
			return [self.scene_id, self.tag_id]

class MoviesScenesRow(TableRow):
	def __init__(self):
		super().__init__('movies_scenes')
		self._movie_id = None
		self._scene_id = None
		self._scene_index = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def movie_id(self):
		return self._movie_id

	@movie_id.setter
	def movie_id(self, movie_id):
		self._movie_id = movie_id

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def scene_index(self):
		return self._scene_index

	@scene_index.setter
	def scene_index(self, scene_index):
		self._scene_index = scene_index

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.movie_id, self.scene_id, self.scene_index]
		else:
			return [self.movie_id, self.scene_id, self.scene_index]

class ScenesCoverRow(TableRow):
	def __init__(self):
		super().__init__('scenes_cover')
		self._scene_id = None
		self._cover = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def cover(self):
		return self._cover

	@cover.setter
	def cover(self, cover):
		self._cover = cover

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.cover]
		else:
			return [self.scene_id, self.cover]

class PerformersImagesRow(TableRow):
	def __init__(self):
		super().__init__('performers_images')
		self._performer_id = None
		self._image_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def image_id(self):
		return self._image_id

	@image_id.setter
	def image_id(self, image_id):
		self._image_id = image_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.image_id]
		else:
			return [self.performer_id, self.image_id]

class ImagesTagsRow(TableRow):
	def __init__(self):
		super().__init__('images_tags')
		self._image_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def image_id(self):
		return self._image_id

	@image_id.setter
	def image_id(self, image_id):
		self._image_id = image_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.image_id, self.tag_id]
		else:
			return [self.image_id, self.tag_id]

class SceneStashIdsRow(TableRow):
	def __init__(self):
		super().__init__('scene_stash_ids')
		self._scene_id = None
		self._endpoint = None
		self._stash_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def endpoint(self):
		return self._endpoint

	@endpoint.setter
	def endpoint(self, endpoint):
		self._endpoint = endpoint

	@property
	def stash_id(self):
		return self._stash_id

	@stash_id.setter
	def stash_id(self, stash_id):
		self._stash_id = stash_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.endpoint, self.stash_id]
		else:
			return [self.scene_id, self.endpoint, self.stash_id]

class ScenesGalleriesRow(TableRow):
	def __init__(self):
		super().__init__('scenes_galleries')
		self._scene_id = None
		self._gallery_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.gallery_id]
		else:
			return [self.scene_id, self.gallery_id]

class GalleriesImagesRow(TableRow):
	def __init__(self):
		super().__init__('galleries_images')
		self._gallery_id = None
		self._image_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	@property
	def image_id(self):
		return self._image_id

	@image_id.setter
	def image_id(self, image_id):
		self._image_id = image_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.gallery_id, self.image_id]
		else:
			return [self.gallery_id, self.image_id]

class PerformersGalleriesRow(TableRow):
	def __init__(self):
		super().__init__('performers_galleries')
		self._performer_id = None
		self._gallery_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.gallery_id]
		else:
			return [self.performer_id, self.gallery_id]

class GalleriesTagsRow(TableRow):
	def __init__(self):
		super().__init__('galleries_tags')
		self._gallery_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.gallery_id, self.tag_id]
		else:
			return [self.gallery_id, self.tag_id]

class PerformersTagsRow(TableRow):
	def __init__(self):
		super().__init__('performers_tags')
		self._performer_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.tag_id]
		else:
			return [self.performer_id, self.tag_id]

class TagAliasesRow(TableRow):
	def __init__(self):
		super().__init__('tag_aliases')
		self._tag_id = None
		self._alias = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	@property
	def alias(self):
		return self._alias

	@alias.setter
	def alias(self, alias):
		self._alias = alias

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.tag_id, self.alias]
		else:
			return [self.tag_id, self.alias]

class StudioAliasesRow(TableRow):
	def __init__(self):
		super().__init__('studio_aliases')
		self._studio_id = None
		self._alias = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def alias(self):
		return self._alias

	@alias.setter
	def alias(self, alias):
		self._alias = alias

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.studio_id, self.alias]
		else:
			return [self.studio_id, self.alias]

class SqliteStat1Row(TableRow):
	def __init__(self):
		super().__init__('sqlite_stat1')
		self._tbl = None
		self._idx = None
		self._stat = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def tbl(self):
		return self._tbl

	@tbl.setter
	def tbl(self, tbl):
		self._tbl = tbl

	@property
	def idx(self):
		return self._idx

	@idx.setter
	def idx(self, idx):
		self._idx = idx

	@property
	def stat(self):
		return self._stat

	@stat.setter
	def stat(self, stat):
		self._stat = stat

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.tbl, self.idx, self.stat]
		else:
			return [self.tbl, self.idx, self.stat]

class SqliteStat4Row(TableRow):
	def __init__(self):
		super().__init__('sqlite_stat4')
		self._tbl = None
		self._idx = None
		self._neq = None
		self._nlt = None
		self._ndlt = None
		self._sample = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def tbl(self):
		return self._tbl

	@tbl.setter
	def tbl(self, tbl):
		self._tbl = tbl

	@property
	def idx(self):
		return self._idx

	@idx.setter
	def idx(self, idx):
		self._idx = idx

	@property
	def neq(self):
		return self._neq

	@neq.setter
	def neq(self, neq):
		self._neq = neq

	@property
	def nlt(self):
		return self._nlt

	@nlt.setter
	def nlt(self, nlt):
		self._nlt = nlt

	@property
	def ndlt(self):
		return self._ndlt

	@ndlt.setter
	def ndlt(self, ndlt):
		self._ndlt = ndlt

	@property
	def sample(self):
		return self._sample

	@sample.setter
	def sample(self, sample):
		self._sample = sample

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.tbl, self.idx, self.neq, self.nlt, self.ndlt, self.sample]
		else:
			return [self.tbl, self.idx, self.neq, self.nlt, self.ndlt, self.sample]

