from sc2sim import SC2Env, SC2Action

def test_marine_should_walk_top():
    _test_walk_step((0, 0), SC2Action.TOP, (0, 1))

def test_marine_should_walk_topright():
    _test_walk_step((0, 0), SC2Action.TOP_RIGHT, (1, 1))

def test_marine_should_walk_topleft():
    _test_walk_step((1, 0), SC2Action.TOP_LEFT, (0, 1))

def test_marine_should_walk_right():
    _test_walk_step((0, 0), SC2Action.RIGHT, (1, 0))

def test_marine_should_walk_left():
    _test_walk_step((1, 0), SC2Action.LEFT, (0, 0))

def test_marine_should_walk_bottom():
    _test_walk_step((0, 1), SC2Action.BOT, (0, 0))

def test_marine_should_walk_bottomright():
    _test_walk_step((0, 1), SC2Action.BOT_RIGHT, (1, 0))

def test_marine_should_walk_bottomleft():
    _test_walk_step((1, 1), SC2Action.BOT_LEFT, (0, 0))

def test_marine_should_stay_within_world_bounds_at_botleft_corner():
    _test_walk_step((0, 1), SC2Action.BOT_LEFT, (0, 0))
    _test_walk_step((1, 0), SC2Action.BOT_LEFT, (0, 0))
    _test_walk_step((0, 0), SC2Action.BOT_LEFT, (0, 0))

def test_marine_should_stay_within_world_bounds_at_botright_corner():
    _test_walk_step((128, 1), SC2Action.BOT_RIGHT, (128, 0), env_width=128, env_height=128)
    _test_walk_step((127, 0), SC2Action.BOT_RIGHT, (128, 0), env_width=128, env_height=128)
    _test_walk_step((128, 0), SC2Action.BOT_RIGHT, (128, 0), env_width=128, env_height=128)

def test_marine_should_stay_within_world_bounds_at_topright_corner():
    _test_walk_step((128, 127), SC2Action.TOP_RIGHT, (128, 128), env_width=128, env_height=128)
    _test_walk_step((127, 128), SC2Action.TOP_RIGHT, (128, 128), env_width=128, env_height=128)
    _test_walk_step((128, 128), SC2Action.TOP_RIGHT, (128, 128), env_width=128, env_height=128)

def test_marine_should_stay_within_world_bounds_at_topleft_corner():
    _test_walk_step((0, 127), SC2Action.TOP_LEFT, (0, 128), env_width=128, env_height=128)
    _test_walk_step((1, 128), SC2Action.TOP_LEFT, (0, 128), env_width=128, env_height=128)
    _test_walk_step((0, 128), SC2Action.TOP_LEFT, (0, 128), env_width=128, env_height=128)

def _test_walk_step(pos_before, action, pos_after, env_width=128, env_height=128):
    env = SC2Env(world_width=env_width, world_height=env_height, norm_marine_pos=pos_before)
    env.step(action)
    assert(env.marine_pos == pos_after)
