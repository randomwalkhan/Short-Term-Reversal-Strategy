# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 14:55:01 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$32,735.80`
- Equity: `$65,311.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option WMT261023C00108000       2026-09-17                   0    127     32575.5                 32575.5         2.57           2.57      106.54        106.57          bid_ask_mid                       2.57                bid_ask_mid                    True             0.0                    0.0         83.33               24              0.89         24.93           24.89                  39.87                 249.0           74.0               0.12                      ok
```

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           84.00               25            0.87              0.65        107.22                39.87         0.568            pass              0.357             31.1                           0.327                0.45              0.076                                 ok            True                  False
   TRI           91.67               24            1.88              1.33        100.74                57.96         0.566            pass              0.524             20.8                           0.302               -6.10             -0.595 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.38               32            0.77              1.19        219.80                56.33         0.548            pass              0.487             56.4                           0.524               -9.57             -0.462 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.00               40            0.83              0.78        134.66                64.77         0.521            pass              0.602             27.7                           0.158              -15.78             -1.351 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.89               18            0.37              0.35        134.19                14.34         0.518            pass              0.536             64.5                           0.568               -3.74             -0.358            downtrend_blocked_slope           False                  False
  NFLX           85.00               20            1.39              0.75         76.09                36.27         0.517            pass              0.252              0.0                           0.160               -8.93             -0.625 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.55               29            0.25              0.49        272.98                24.48         0.515            pass              0.831             84.3                           0.632               -2.46             -0.133                                 ok           False                  False
  INTU          100.00               26            1.40              3.13        316.79                44.10         0.510            pass              0.616             19.5                           0.137               -8.54             -0.588 downtrend_blocked_slope_and_streak           False                  False
  CTSH          100.00               38            0.24              0.10         61.81                43.69         0.508            pass              0.883             81.7                           0.598               -2.68             -0.092                                 ok           False                  False
  VRSK           80.00               10            2.64              3.36        180.31                41.00         0.499 below_threshold              0.119             23.2                           0.393               -5.70             -0.401            downtrend_blocked_slope           False                  False
 CMCSA           87.50                8            2.63              0.44         23.54                34.54         0.492 below_threshold              0.256              2.3                           0.191              -13.82             -1.401 downtrend_blocked_slope_and_streak           False                  False
  PAYX           89.66               29            0.57              0.46        116.52                25.45         0.490 below_threshold              0.601             56.0                           0.485               -6.40             -0.597            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-17T14:55:01.186160-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-17T14:50:04.102358-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"allocated_cash": 32575.5, "asset_type": "option", "contract_symbol": "WMT261023C00108000", "contracts": 127, "early_entry_score": 0.327, "entry_mode": "regular", "entry_option_price": 2.565, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 249.0, "option_spread_pct": 12.09, "option_volume": 74.0, "success_rate": 83.33, "ticker": "WMT", "timing_score": 0.572}
2026-09-17T14:50:04.102358-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-17", "training_samples": 5767, "window": 5}
2026-09-17T12:00:02.509358-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:55:04.328741-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:50:05.315984-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:45:05.877889-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:40:01.171788-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:35:02.981434-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:30:02.332975-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "CTSH261016C00060000", "current_drop_pct": 0.52, "early_entry_score": 0.801, "early_reclaim_pct": 61.0, "entry_ask": 3.9, "entry_bid": 3.5, "entry_mode": "early", "entry_option_price": 3.7, "hypothetical_budget": 32655.65, "hypothetical_contracts": 88, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 756.0, "option_spread_pct": 10.81, "option_volume": 37.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.801, "early_reclaim_pct": 61.0, "matched_signals": 35, "recovery_stability_score": 0.604, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.51, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917145501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917145501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917145501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917145501)

</details>
