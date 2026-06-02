# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 09:30:05 EDT`
Last processed slot: `manage_0930`

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
  MELI           94.74               38            0.66              7.95       1727.57                60.28         0.602          pass              0.818             59.4                           0.418                8.43              0.774                                 ok            True                  False
  INTC           95.65               23            2.50              1.91        108.51                88.85         0.551          pass              0.548              2.2                           0.161               -1.45             -0.164                                 ok            True                  False
  UPRO           93.94               33            0.56              0.59        150.08                29.00         0.514          pass              0.743             55.5                           0.540                7.27              0.922                                 ok            True                  False
  CDNS           89.47               19            2.00              5.81        411.67                44.19         0.510          pass              0.459             31.7                           0.409               17.30              1.721                                 ok            True                  False
  ROST           93.55               31            0.64              1.01        223.64                42.05         0.504          pass              0.794             80.9                           0.667                5.47              0.678                                 ok            True                   True
    ZS           81.25               16            3.14              3.42        154.24               157.27         0.834          pass              0.295             46.0                           0.474              -13.66             -2.534            downtrend_blocked_slope           False                  False
  INSM           71.43               28            1.83              1.36        105.45               110.78         0.745          pass              0.318             41.0                           0.390               -2.86             -0.222                                 ok           False                  False
  QCOM           97.62               42            0.07              0.12        228.94               102.92         0.677          pass              0.960             97.6                           0.576               12.36              1.908                                 ok           False                  False
  FTNT          100.00                8            2.85              2.94        145.88                71.69         0.663          pass              0.567             33.5                           0.446               13.00              1.196                                 ok           False                  False
  SHOP           75.00               24            2.34              2.04        123.25                84.68         0.613          pass              0.240             28.5                           0.360               18.38              2.050                                 ok           False                  False
   TRI           70.59               17            1.53              1.01         93.53                62.66         0.601          pass              0.107              0.0                           0.261                3.58              0.426                                 ok           False                  False
  REGN           90.24               41            0.16              0.66        600.38                42.53         0.532          pass              0.766             79.8                           0.578               -4.62             -0.612 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602093005)

</details>
