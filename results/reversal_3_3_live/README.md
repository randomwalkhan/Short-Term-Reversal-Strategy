# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 10:05:05 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$37,600.60`
- Equity: `$79,675.60`
- Realized PnL: `$64,478.10`
- Unrealized PnL: `$5,197.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261016C00110000       2026-09-03                   1     99     36877.5                 42075.0         3.72           4.25      108.86        109.74          bid_ask_mid                       4.25                bid_ask_mid                    True          5197.5                  14.09         89.19               37              0.54         28.76           30.03                  36.36                2875.0          348.0               0.04                      ok
```

## Today's Closed Trades (2026-09-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               11            1.44              4.48        442.20                21.54         0.553          pass              0.551             29.8                           0.216               -0.37             -0.035                                 ok            True                  False
  PAYX          100.00               12            1.57              1.38        124.49                25.54         0.549          pass              0.596             42.6                           0.595               -1.10             -0.082                                 ok            True                  False
    ZS          100.00               21            2.56              3.19        176.43                62.66         0.528          pass              0.719             64.2                           0.745               -4.68             -0.024                                 ok            True                  False
 CMCSA           92.86               28            0.51              0.09         26.61                25.91         0.524          pass              0.596             27.0                           0.284               -1.25             -0.191                                 ok            True                  False
  REGN          100.00               21            1.05              6.19        840.82                28.19         0.518          pass              0.579             18.1                           0.137                0.07              0.138                                 ok            True                  False
  NFLX           85.71               21            1.46              0.85         82.31                32.95         0.518          pass              0.345             22.4                           0.246                2.35              0.240                                 ok            True                  False
  CHTR           90.91               44            0.57              0.61        151.12                61.35         0.506          pass              0.653             37.3                           0.263                0.23              0.035                                 ok            True                  False
  WDAY           85.71               21            3.79              5.49        204.57                73.93         0.501          pass              0.361             28.6                           0.472               -0.46              0.296                                 ok            True                  False
  PYPL          100.00                9            2.27              0.90         56.43                56.63         0.626          pass              0.565             34.2                           0.525               -9.78             -1.562 downtrend_blocked_slope_and_streak           False                  False
  SNPS           85.71                7            3.00              8.74        412.56                57.80         0.607          pass              0.213              0.0                           0.150                1.50              0.281                                 ok           False                  False
  MSTR           77.78               27            2.74              2.78        143.63               101.55         0.596          pass              0.348             58.2                           0.755               18.11              1.277                                 ok           False                  False
  MELI          100.00               38            0.33              4.57       1989.09                45.76         0.534          pass              0.862             73.9                           0.612                3.21              0.251                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-04T10:05:05.442075-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:00:02.334638-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T00:00:05.130277-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 93}
2026-09-03T15:10:05.000086-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T15:05:01.989817-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T14:55:01.997283-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-03T14:50:04.996854-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                 {"early_entry_score": 0.577, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 18.28, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "REGN", "timing_score": 0.533}
2026-09-03T14:50:04.996854-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-03", "training_samples": 5764, "window": 5}
2026-09-03T14:50:04.996854-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                              {"early_entry_score": 0.72, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 85.0, "option_spread_pct": 12.16, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.542}
2026-09-03T14:50:04.996854-04:00       entry_1500                   entry {"allocated_cash": 36877.5, "asset_type": "option", "contract_symbol": "CSCO261016C00110000", "contracts": 99, "early_entry_score": 0.681, "entry_mode": "regular", "entry_option_price": 3.725, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2875.0, "option_spread_pct": 4.03, "option_volume": 348.0, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.511}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904100505)

</details>
