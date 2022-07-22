
from telelib.bot import DefaultType

# @url https://core.telegram.org/bots/api#inlinequeryresultcachedphoto# ['Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.']
class InlineQueryResultCachedPhoto(DefaultType):

    
	# @var type Type of the result, must be photo
	@property
	def type(self) -> String:
		return self._d["type"]
	# @var id Unique identifier for this result, 1-64 bytes
	@property
	def id(self) -> String:
		return self._d["id"]
	# @var photo_file_id A valid file identifier of the photo
	@property
	def photo_file_id(self) -> String:
		return self._d["photo_file_id"]
	# @var title Optional. Title for the result
	@property
	def title(self) -> String:
		return self._d["title"]
	# @var description Optional. Short description of the result
	@property
	def description(self) -> String:
		return self._d["description"]
	# @var caption Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
	@property
	def caption(self) -> String:
		return self._d["caption"]
	# @var parse_mode Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
	@property
	def parse_mode(self) -> String:
		return self._d["parse_mode"]
	# @var caption_entities Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
	@property
	def caption_entities(self) -> Array of MessageEntity:
		return self._d["caption_entities"]
	# @var reply_markup Optional. Inline keyboard attached to the message
	@property
	def reply_markup(self) -> InlineKeyboardMarkup:
		return self._d["reply_markup"]
	# @var input_message_content Optional. Content of the message to be sent instead of the photo
	@property
	def input_message_content(self) -> InputMessageContent:
		return self._d["input_message_content"]

