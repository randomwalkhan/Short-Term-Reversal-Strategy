# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 16:00:04 EDT`
Last processed slot: `manage_1600`

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
   WMT     option         option WMT261023C00108000       2026-09-17                   0    127     32575.5                 32575.5         2.57           2.57      106.54        106.77          bid_ask_mid                       2.57                bid_ask_mid                    True             0.0                    0.0         83.33               24              0.89         24.93           24.12                  39.87                 249.0           74.0               0.12                      ok
```

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           84.38               32            0.68              0.51        107.28                39.87         0.539            pass              0.456             46.2                           0.569                0.64              0.085                                 ok            True                  False
  PANW           82.61               46            0.16              0.41        375.47                80.65         0.581            pass              0.616             96.1                           0.699               14.18              1.552                                 ok           False                  False
   TRI           91.67               24            1.84              1.30        100.75                57.96         0.568            pass              0.529             22.5                           0.379               -6.06             -0.594 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.38               32            0.76              1.17        219.81                56.33         0.549            pass              0.490             57.3                           0.613               -9.55             -0.461 downtrend_blocked_slope_and_streak           False                  False
  NFLX           84.21               19            1.45              0.78         76.08                36.27         0.518            pass              0.224              0.0                           0.210               -8.98             -0.628 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.55               29            0.29              0.56        272.95                24.48         0.513            pass              0.823             81.7                           0.719               -2.50             -0.135                                 ok           False                  False
   PEP           88.24               17            0.54              0.51        134.12                14.34         0.513            pass              0.462             48.2                           0.292               -3.90             -0.366            downtrend_blocked_slope           False                  False
  INTU          100.00               26            1.52              3.39        316.68                44.10         0.503            pass              0.595             12.8                           0.256               -8.65             -0.593 downtrend_blocked_slope_and_streak           False                  False
  CHTR           89.74               39            1.16              1.10        134.53                64.77         0.502            pass              0.617             37.9                           0.463              -16.07             -1.366 downtrend_blocked_slope_and_streak           False                  False
  VRSK           80.00               10            2.86              3.63        180.19                41.00         0.487 below_threshold              0.099             16.8                           0.321               -5.91             -0.411            downtrend_blocked_slope           False                  False
  SHOP           85.29               34            1.03              0.94        129.56                49.93         0.476 below_threshold              0.475             42.2                           0.573               -9.34             -1.157 downtrend_blocked_slope_and_streak           False                  False
   ROP           97.14               35            0.30              0.80        375.48                28.32         0.475 below_threshold              0.850             78.5                           0.498               -9.89             -1.068 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-17T15:10:01.182099-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-17T15:05:01.143983-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-17T15:00:04.868136-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-17T14:55:01.186160-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-17T14:50:04.102358-04:00       entry_1500              entry {"allocated_cash": 32575.5, "asset_type": "option", "contract_symbol": "WMT261023C00108000", "contracts": 127, "early_entry_score": 0.327, "entry_mode": "regular", "entry_option_price": 2.565, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 249.0, "option_spread_pct": 12.09, "option_volume": 74.0, "success_rate": 83.33, "ticker": "WMT", "timing_score": 0.572}
2026-09-17T14:50:04.102358-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-17", "training_samples": 5767, "window": 5}
2026-09-17T12:00:02.509358-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:55:04.328741-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:50:05.315984-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T11:45:05.877889-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917160004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917160004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917160004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917160004)

</details>
