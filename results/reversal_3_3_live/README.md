# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 10:10:01 EDT`
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

- Cash: `$81,160.60`
- Equity: `$81,160.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-04)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261016C00110000     99          2026-09-03         2026-09-04        3.725         4.4 6682.5   18.120805 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               13            1.21              3.75        442.51                21.54         0.553          pass              0.599             41.2                           0.288               -0.13             -0.024                                 ok            True                  False
  PAYX          100.00               11            1.76              1.54        124.42                25.54         0.545          pass              0.569             35.9                           0.573               -1.29             -0.090                                 ok            True                  False
  NFLX           88.24               17            1.72              1.00         82.24                32.95         0.531          pass              0.345              8.7                           0.103                2.08              0.228                                 ok            True                  False
    ZS          100.00               12            3.71              4.61        175.82                62.66         0.515          pass              0.610             48.3                           0.501               -5.80             -0.077                                 ok            True                  False
  CHTR           90.91               44            0.52              0.55        151.14                61.35         0.509          pass              0.670             42.8                           0.249                0.28              0.037                                 ok            True                  False
  WDAY           81.25               16            4.08              5.91        204.39                73.93         0.509          pass              0.193             23.0                           0.381               -0.77              0.282                                 ok            True                  False
  MSFT           89.47               19            1.31              4.67        508.12                22.07         0.506          pass              0.393             10.0                           0.210                4.18              0.402                                 ok            True                  False
  REGN          100.00               25            0.90              5.32        841.19                28.19         0.502          pass              0.639             29.6                           0.200                0.22              0.145                                 ok            True                  False
  CRWD           91.49               47            0.11              0.16        214.90                92.33         0.645          pass              0.849             92.9                           0.507               11.87              1.444                                 ok           False                  False
  PYPL          100.00                6            2.85              1.13         56.33                56.63         0.611          pass              0.513             17.3                           0.338              -10.32             -1.589 downtrend_blocked_slope_and_streak           False                  False
  SNPS           83.33                6            3.30              9.62        412.19                57.80         0.590          pass              0.155              2.4                           0.044                1.18              0.267                                 ok           False                  False
  MSTR           76.00               25            3.14              3.18        143.46               101.55         0.583          pass              0.315             52.2                           0.684               17.63              1.258                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                     detail
2026-09-04T10:10:01.256246-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:10:01.256246-04:00      manage_1000                    exit                                                                      {"asset_type": "option", "contract_symbol": "CSCO261016C00110000", "fill_price": 4.4, "pnl": 6682.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.12, "ticker": "CSCO"}
2026-09-04T10:05:05.442075-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T10:00:02.334638-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T00:00:05.130277-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 93}
2026-09-03T15:10:05.000086-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-03T15:05:01.989817-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-03T14:55:01.997283-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-03T14:50:04.996854-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.72, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 85.0, "option_spread_pct": 12.16, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.542}
2026-09-03T14:50:04.996854-04:00       entry_1500          timing_overlay                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-03", "training_samples": 5764, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904101001)

</details>
