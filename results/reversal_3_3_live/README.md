# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:30:04 EDT`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$33,669.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               12            2.08              2.14        146.22                71.69         0.685          pass              0.637             51.6                           0.753               13.90              1.232                                 ok            True                  False
  MNST           93.33               15            1.59              0.99         88.67                49.60         0.644          pass              0.453              0.0                           0.190               -0.97              0.167                                 ok            True                  False
  MELI           92.00               25            1.72             20.84       1722.05                60.28         0.599          pass              0.605             41.6                           0.660                7.27              0.725                                 ok            True                  False
  AMGN           87.50               16            1.01              2.33        328.13                20.27         0.530          pass              0.447             51.2                           0.700                0.43              0.031                                 ok            True                  False
  CDNS           89.47               19            1.99              5.77        411.69                44.19         0.508          pass              0.475             37.2                           0.476               17.32              1.722                                 ok            True                  False
    MU           83.33               36            0.20              1.47       1034.11               101.73         0.742          pass              0.604             89.2                           0.473               51.52              4.632                                 ok           False                  False
  INSM           33.33                6            4.74              3.52        104.52               110.78         0.644          pass              0.089              8.0                           0.154               -5.74             -0.359            downtrend_blocked_slope           False                  False
    ZS          100.00                2            8.72              9.50        151.64               157.27         0.585          pass              0.484              8.5                           0.291              -18.64             -2.804            downtrend_blocked_slope           False                  False
   WMT           84.21               19            1.12              0.90        114.22                32.65         0.558          pass              0.306             26.0                           0.278              -15.01             -1.698 downtrend_blocked_slope_and_streak           False                  False
   HON           77.78                9            1.43              2.37        235.52                24.20         0.550          pass              0.055              0.0                           0.202                7.33              0.965                                 ok           False                  False
  REGN           88.24               34            0.69              2.91        599.41                42.53         0.532          pass              0.596             54.5                           0.647               -5.13             -0.637 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.29               35            0.23              0.24        150.19                29.00         0.523          pass              0.844             81.5                           0.718                7.60              0.936                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                 detail
2026-06-02T10:30:04.405006-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:25:01.235572-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:20:01.327977-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015 entry_candidate_skipped {"early_entry_score": 0.679, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 117.0, "option_spread_pct": 24.24, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.442}
2026-06-02T10:10:06.260122-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:05:01.451088-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:00:02.499087-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T09:20:05.650957-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                          {'saved': 92}
2026-06-01T15:10:04.135705-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602103004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602103004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602103004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602103004)

</details>
