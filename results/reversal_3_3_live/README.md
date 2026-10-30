# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 15:40:02 EDT`
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

- Cash: `$58,976.55`
- Equity: `$117,326.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$150.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-10-30                   0     30     58200.0                 58350.0         19.4          19.45      259.39        260.84          bid_ask_mid                      19.45                bid_ask_mid                    True           150.0                   0.26          84.0               25              1.96         51.59           51.79                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-10-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  MSTR     option         option MSTR261218C00140000     41          2026-10-29         2026-10-30       15.025     13.5225 -6160.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.71               28            1.38              2.55        263.49                64.38         0.605            pass              0.495             54.0                           0.503               -3.85             -0.258                                 ok            True                  False
  AAPL           91.67               12            1.38              3.38        347.46                13.86         0.517            pass              0.485             36.3                           0.437                0.18              0.111                                 ok            True                  False
  FTNT           82.35               17            2.62              2.55        138.01                91.61         0.662            pass              0.243             22.6                           0.476              -19.91             -1.557            downtrend_blocked_slope           False                  False
 GOOGL           76.92               13            1.78              3.54        282.30                51.94         0.644            pass              0.164             26.7                           0.513              -18.15             -1.838 downtrend_blocked_slope_and_streak           False                  False
  GOOG           70.00               10            1.90              3.75        280.71                50.42         0.641            pass              0.133             23.1                           0.468              -17.79             -1.787 downtrend_blocked_slope_and_streak           False                  False
  FAST           88.89                9            1.11              0.41         52.37                21.92         0.566            pass              0.328             11.4                           0.237                2.37              0.198                                 ok           False                  False
  ALNY           75.00                4            5.31              6.47        171.23               108.34         0.560            pass              0.065              2.8                           0.081              -28.93             -2.584            downtrend_blocked_slope           False                  False
  META           68.75               16            1.55              6.78        621.62                38.13         0.551            pass              0.206             37.0                           0.378              -13.32             -1.674 downtrend_blocked_slope_and_streak           False                  False
  MELI           68.18               22            1.89             21.94       1650.73                48.11         0.539            pass              0.246             37.5                           0.512              -11.19             -1.491 downtrend_blocked_slope_and_streak           False                  False
  ROST           73.33               15            1.57              2.55        231.21                24.69         0.504            pass              0.084              0.0                           0.226               -3.47             -0.409            downtrend_blocked_slope           False                  False
  MSFT          100.00               17            1.35              5.00        528.00                19.58         0.499 below_threshold              0.661             54.8                           0.717               -1.14             -0.065                                 ok           False                  False
  ABNB           87.50               24            1.32              1.54        165.79                25.92         0.497 below_threshold              0.356              4.3                           0.219               -5.44             -0.696 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-30T15:10:04.962037-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-30T15:05:04.984730-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-30T15:00:07.087528-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-30T14:55:05.117315-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-30T14:50:03.931152-04:00       entry_1500              entry {"allocated_cash": 58200.0, "asset_type": "option", "contract_symbol": "CEG261218C00260000", "contracts": 30, "early_entry_score": 0.369, "entry_mode": "regular", "entry_option_price": 19.4, "execution_mode": "option", "matched_signals": 25, "option_liquidity_status": "ok", "option_open_interest": 503.0, "option_spread_pct": 8.25, "option_volume": 30.0, "success_rate": 84.0, "ticker": "CEG", "timing_score": 0.589}
2026-10-30T14:50:03.931152-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-30", "training_samples": 6237, "window": 5}
2026-10-30T12:00:06.415858-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:55:05.950697-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:50:06.698728-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:45:05.073767-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030154002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030154002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030154002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030154002)

</details>
