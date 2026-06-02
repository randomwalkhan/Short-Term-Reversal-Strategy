# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 09:55:05 EDT`
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
  MELI           91.67               12            2.47             29.99       1718.13                60.28         0.641          pass              0.389              0.3                           0.074                6.45              0.690                                 ok            True                  False
  MNST           95.65               23            1.02              0.63         88.83                49.60         0.638          pass              0.552              0.5                           0.025               -0.39              0.194                                 ok            True                  False
  INTC           95.65               23            2.41              1.85        108.54                88.85         0.532          pass              0.686             48.8                           0.500               -1.37             -0.160                                 ok            True                  False
  CDNS           93.33               15            2.26              6.55        411.35                44.19         0.523          pass              0.527             28.7                           0.331               17.00              1.709                                 ok            True                  False
  INSM           37.50                8            4.51              3.35        104.60               110.78         0.651          pass              0.103             12.6                           0.142               -5.51             -0.348            downtrend_blocked_slope           False                  False
  FTNT          100.00                7            3.24              3.33        145.71                71.69         0.647          pass              0.539             24.7                           0.357               12.55              1.178                                 ok           False                  False
    ZS          100.00                2            9.04              9.86        151.49               157.27         0.566          pass              0.464              2.4                           0.172              -18.92             -2.820            downtrend_blocked_slope           False                  False
  AMGN           85.71                7            1.50              3.45        327.65                20.27         0.563          pass              0.247             12.7                           0.237               -0.06              0.008                                 ok           False                  False
   WMT           87.50               24            0.86              0.69        114.31                32.65         0.549          pass              0.429             26.9                           0.349              -14.79             -1.686 downtrend_blocked_slope_and_streak           False                  False
  REGN           85.19               27            1.12              4.70        598.65                42.53         0.548          pass              0.386             26.6                           0.261               -5.53             -0.656 downtrend_blocked_slope_and_streak           False                  False
  ISRG          100.00                6            3.14              9.07        408.37                38.26         0.517          pass              0.494             14.2                           0.236               -9.23             -0.952 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.29               35            0.45              0.47        150.13                29.00         0.508          pass              0.793             64.7                           0.679                7.39              0.928                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                detail
2026-06-02T09:20:05.650957-04:00     data_refresh   data_refresh                                                                                                                                                                         {'saved': 92}
2026-06-01T15:10:04.135705-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:00:02.274373-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:55:05.958850-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:50:06.115038-04:00       entry_1500  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T14:50:06.115038-04:00       entry_1500 timing_overlay                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-01", "training_samples": 5165, "window": 5}
2026-06-01T12:50:07.149920-04:00      manage_1300           exit {"asset_type": "option", "contract_symbol": "SNPS260717C00470000", "fill_price": 42.3, "pnl": 2820.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.0, "ticker": "SNPS"}
2026-06-01T12:00:03.957402-04:00 early_entry_1200  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:55:05.058620-04:00 early_entry_1155  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602095505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602095505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602095505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602095505)

</details>
