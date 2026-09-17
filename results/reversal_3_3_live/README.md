# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 15:25:08 EDT`
Last processed slot: `manage_1530`

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
   WMT     option         option WMT261023C00108000       2026-09-17                   0    127     32575.5                 32575.5         2.57           2.57      106.54        106.71          bid_ask_mid                       2.57                bid_ask_mid                    True             0.0                    0.0         83.33               24              0.89         24.93           24.56                  39.87                 249.0           74.0               0.12                      ok
```

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           83.33               30            0.73              0.55        107.26                39.87         0.546            pass              0.402             41.9                           0.570                0.59              0.082                                 ok            True                  False
   TRI           91.67               24            1.76              1.25        100.78                57.96         0.573            pass              0.539             25.8                           0.466               -5.99             -0.590 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.38               32            0.97              1.49        219.67                56.33         0.536            pass              0.454             45.5                           0.379               -9.74             -0.471 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.43               28            0.37              0.70        272.89                24.48         0.514            pass              0.803             77.3                           0.526               -2.57             -0.138                                 ok           False                  False
  INTU          100.00               28            1.17              2.60        317.01                44.10         0.512            pass              0.670             33.0                           0.296               -8.32             -0.577 downtrend_blocked_slope_and_streak           False                  False
  CTSH          100.00               38            0.26              0.11         61.80                43.69         0.507            pass              0.879             80.5                           0.693               -2.70             -0.092                                 ok           False                  False
  CHTR           89.74               39            1.22              1.15        134.51                64.77         0.503            pass              0.517              4.4                           0.143              -16.11             -1.369 downtrend_blocked_slope_and_streak           False                  False
  NFLX           89.66               29            1.09              0.58         76.16                36.27         0.487 below_threshold              0.501             22.7                           0.454               -8.65             -0.611 downtrend_blocked_slope_and_streak           False                  False
  VRSK           77.78                9            2.89              3.68        180.17                41.00         0.487 below_threshold              0.096             15.7                           0.248               -5.95             -0.413            downtrend_blocked_slope           False                  False
  PAYX           87.10               31            0.37              0.30        116.59                25.45         0.486 below_threshold              0.591             71.0                           0.676               -6.22             -0.588            downtrend_blocked_slope           False                  False
   ROP           97.22               36            0.21              0.55        375.59                28.32         0.475 below_threshold              0.877             85.3                           0.647               -9.80             -1.063 downtrend_blocked_slope_and_streak           False                  False
  SHOP           87.50               32            1.31              1.19        129.45                49.93         0.473 below_threshold              0.474             26.7                           0.420               -9.59             -1.170 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917152508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917152508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917152508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917152508)

</details>
