# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 15:55:02 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$36,331.75`
- Equity: `$36,331.75`
- Realized PnL: `$26,331.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-02)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AMZN     option         option AMZN260717C00260000     15          2026-06-02         2026-06-02         10.8      12.575 2662.5   16.435185 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           96.30               27            0.77              0.48         88.89                49.60         0.617            pass              0.764             63.1                           0.627               -0.15              0.205                                 ok            True                  False
  INTC           96.30               27            1.55              1.19        108.82                88.85         0.565            pass              0.771             67.1                           0.591               -0.50             -0.120                                 ok            True                  False
  CRWD           81.25               16            1.92             10.52        777.66                48.77         0.513            pass              0.302             59.1                           0.703               23.97              2.197                                 ok            True                  False
  INSM           71.43               28            1.91              1.42        105.42               110.78         0.723            pass              0.381             63.0                           0.756               -2.94             -0.226                                 ok           False                  False
  MELI           87.50                8            3.40             41.18       1713.33                60.28         0.586            pass              0.300             13.8                           0.389                5.44              0.647                                 ok           False                  False
    ZS           50.00                4            7.60              8.29        152.16               157.27         0.581            pass              0.132             24.6                           0.546              -17.64             -2.749            downtrend_blocked_slope           False                  False
   WMT           75.00               12            1.49              1.19        114.09                32.65         0.569            pass              0.097              8.8                           0.237              -15.33             -1.715 downtrend_blocked_slope_and_streak           False                  False
  PAYX           88.89                9            1.54              1.11        101.97                33.30         0.541            pass              0.471             59.9                           0.640                6.74              0.649                                 ok           False                  False
  SBUX           86.67               15            1.02              0.69         96.22                19.05         0.516            pass              0.295             10.9                           0.193              -10.38             -1.116 downtrend_blocked_slope_and_streak           False                  False
  AMZN           85.71               14            1.80              3.29        259.85                24.44         0.499 below_threshold              0.324             31.8                           0.247               -3.13             -0.005                                 ok           False                  False
  DXCM           75.00               20            1.88              0.99         74.45                46.68         0.496 below_threshold              0.232             38.7                           0.456               12.86              1.030                                 ok           False                  False
  TTWO           88.89                9            2.36              3.74        225.38                38.43         0.494 below_threshold              0.420             44.4                           0.665               -8.48             -0.923 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-02T15:10:01.501174-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:05:06.421436-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T15:00:02.491254-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:55:03.460191-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-02T14:50:05.532618-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T14:50:05.532618-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-02", "training_samples": 5173, "window": 5}
2026-06-02T12:00:02.493429-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:55:02.481940-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:50:01.505874-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-02T11:45:06.568755-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602155502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602155502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602155502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602155502)

</details>
