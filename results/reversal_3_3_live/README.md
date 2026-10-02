# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 15:35:06 EDT`
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

- Cash: `$41,269.30`
- Equity: `$81,229.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$-135.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode        instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
    ZS     option         option ZS261120C00200000       2026-10-02                   0     27     40095.0                 39960.0        14.85           14.8      196.86        196.94          bid_ask_mid                       14.8                bid_ask_mid                    True          -135.0                  -0.34         94.59               37              0.97         55.98           55.79                   77.3                 818.0          103.0               0.04                      ok
```

## Today's Closed Trades (2026-10-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           94.74               38            0.93              1.29        198.23                77.30         0.639            pass              0.699             18.6                           0.354               -0.19             -0.510                                 ok            True                  False
  DRAM           81.25               32            0.73              0.31         61.90                54.09         0.576            pass              0.391             51.1                           0.526                3.30             -0.003                                 ok            True                  False
  MSTR           89.29               28            1.95              2.19        159.56                96.54         0.545            pass              0.518             32.1                           0.495                2.24             -0.431                                 ok            True                  False
  AMGN           84.00               25            0.89              2.54        406.18                47.14         0.526            pass              0.354             31.6                           0.328                4.66              0.513                                 ok            True                  False
   TRI           82.35               17            2.41              1.67         98.64                57.35         0.515            pass              0.302             46.9                           0.275                2.73              0.248                                 ok            True                  False
  INTC           87.50               40            0.04              0.04        119.98                73.87         0.621            pass              0.732             90.0                           0.608               10.45              0.131                                 ok           False                  False
   WBD           95.65               46            0.02              0.00         30.95                37.65         0.551            pass              0.805             50.0                           0.318               11.31              0.523                                 ok           False                  False
  SNPS           80.95               42            0.31              1.06        490.09                58.70         0.530            pass              0.514             78.4                           0.581               27.03              1.972                                 ok           False                  False
  TEAM          100.00               36            1.13              1.50        189.27                55.53         0.521            pass              0.728             34.2                           0.431               -2.22             -0.606           downtrend_blocked_streak           False                  False
  PAYX           66.67               12            2.07              1.46        100.21                39.54         0.509            pass              0.082              5.8                           0.200              -14.97             -1.740 downtrend_blocked_slope_and_streak           False                  False
  GILD           85.71                7            1.93              2.00        146.64                19.81         0.488 below_threshold              0.257             18.6                           0.491               -3.64             -0.294 downtrend_blocked_slope_and_streak           False                  False
    MU           92.31               26            2.21             16.98       1090.11                49.88         0.486 below_threshold              0.497              4.4                           0.196                5.64              0.319                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-02T15:10:06.510423-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-02T15:05:02.993202-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-02T15:00:05.745060-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-02T14:55:02.797853-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-02T14:50:06.331180-04:00       entry_1500              entry {"allocated_cash": 40095.0, "asset_type": "option", "contract_symbol": "ZS261120C00200000", "contracts": 27, "early_entry_score": 0.679, "entry_mode": "regular", "entry_option_price": 14.85, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 818.0, "option_spread_pct": 4.04, "option_volume": 103.0, "success_rate": 94.59, "ticker": "ZS", "timing_score": 0.642}
2026-10-02T14:50:06.331180-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-02", "training_samples": 5912, "window": 5}
2026-10-02T12:00:05.856785-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:55:04.675487-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:50:01.924134-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:45:02.865482-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002153506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002153506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002153506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002153506)

</details>
