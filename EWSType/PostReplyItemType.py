##
# Definition of the PostReplyItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PostReplyItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PostReplyItemType (EWSType):
	##
	# NewBodyContent property
	#
	# @var EWSType_BodyType
	#
	self.NewBodyContent=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'NewBodyContent',
		'required' : False,
		'type' : 'BodyType',
		},
		]
# end this->schema
# end function __construct()
# end class PostReplyItemType