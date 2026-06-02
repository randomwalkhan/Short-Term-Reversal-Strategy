# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:05:01 EDT`
Last processed slot: `manage_1000`

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
  MNST           94.12               17            1.47              0.92         88.71                49.60         0.640          pass              0.508              7.1                           0.173               -0.85              0.173                                 ok            True                  False
  MELI           91.67               12            2.50             30.23       1718.02                60.28         0.635          pass              0.434             15.3                           0.176                6.42              0.689                                 ok            True                  False
  INTC           96.15               26            1.59              1.22        108.81                88.85         0.569          pass              0.762             66.3                           0.819               -0.54             -0.122                                 ok            True                  False
   HON           80.00               15            1.02              1.69        235.82                24.20         0.542          pass              0.109              7.1                           0.179                7.78              0.985                                 ok            True                  False
  ROST           93.55               31            0.69              1.08        223.61                42.05         0.500          pass              0.790             79.5                           0.374                5.42              0.676                                 ok            True                  False
  INSM           50.00               12            3.83              2.85        104.81               110.78         0.681          pass              0.159             25.7                           0.472               -4.84             -0.316            downtrend_blocked_slope           False                  False
  FTNT          100.00                7            3.26              3.36        145.70                71.69         0.645          pass              0.537             24.1                           0.266               12.52              1.177                                 ok           False                  False
   WMT           84.21               19            1.05              0.84        114.24                32.65         0.566          pass              0.260             10.4                           0.162              -14.95             -1.695 downtrend_blocked_slope_and_streak           False                  False
    ZS          100.00                2            9.05              9.86        151.48               157.27         0.562          pass              0.471              5.0                           0.172              -18.93             -2.820            downtrend_blocked_slope           False                  False
  AMGN           83.33                6            1.58              3.63        327.57                20.27         0.558          pass              0.217             24.0                           0.257               -0.14              0.005                                 ok           False                  False
  REGN           85.19               27            1.05              4.41        598.77                42.53         0.552          pass              0.400             31.0                           0.278               -5.47             -0.653 downtrend_blocked_slope_and_streak           False                  False
  SHOP           66.67                9            4.56              3.97        122.42                84.68         0.533          pass              0.094             13.5                           0.198               15.69              1.946                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                detail
2026-06-02T10:05:01.451088-04:00 early_entry_1005  entry_skipped                                                                                                                                                            {"reason": "no_candidate"}
2026-06-02T10:00:02.499087-04:00 early_entry_1000  entry_skipped                                                                                                                                                            {"reason": "no_candidate"}
2026-06-02T09:20:05.650957-04:00     data_refresh   data_refresh                                                                                                                                                                         {'saved': 92}
2026-06-01T15:10:04.135705-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:00:02.274373-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:55:05.958850-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:50:06.115038-04:00       entry_1500  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T14:50:06.115038-04:00       entry_1500 timing_overlay                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-01", "training_samples": 5165, "window": 5}
2026-06-01T12:50:07.149920-04:00      manage_1300           exit {"asset_type": "option", "contract_symbol": "SNPS260717C00470000", "fill_price": 42.3, "pnl": 2820.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.0, "ticker": "SNPS"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602100501)

</details>
