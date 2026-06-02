# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 09:45:06 EDT`
Last processed slot: `manual`

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
  FTNT          100.00               11            2.12              2.18        146.21                71.69         0.688          pass              0.628             50.7                           0.752               13.85              1.231                                 ok            True                  False
  MELI           92.00               25            1.75             21.15       1721.91                60.28         0.605          pass              0.548             22.5                           0.307                7.24              0.724                                 ok            True                  False
  CRWD           81.25               16            1.79              9.78        777.98                48.77         0.529          pass              0.296             56.6                           0.590               24.14              2.204                                 ok            True                  False
   ADP          100.00               12            2.30              3.77        232.13                34.26         0.513          pass              0.531             22.3                           0.240                2.43              0.303                                 ok            True                  False
  AMGN           87.50               24            0.72              1.66        328.42                20.27         0.505          pass              0.425             27.0                           0.299                0.73              0.044                                 ok            True                  False
    ZS           50.00                4            6.94              7.56        152.47               157.27         0.644          pass              0.121             18.8                           0.238              -17.05             -2.716            downtrend_blocked_slope           False                  False
  INSM           33.33                6            5.00              3.71        104.44               110.78         0.627          pass              0.072              3.0                           0.191               -6.00             -0.371            downtrend_blocked_slope           False                  False
  SHOP           73.33               15            3.57              3.10        122.79                84.68         0.579          pass              0.139             15.8                           0.256               16.89              1.993                                 ok           False                  False
  MNST           97.62               42            0.37              0.23         89.00                49.60         0.559          pass              0.799             47.6                           0.262                0.26              0.223                                 ok           False                  False
  REGN           85.19               27            1.09              4.57        598.70                42.53         0.553          pass              0.340             11.0                           0.202               -5.50             -0.655 downtrend_blocked_slope_and_streak           False                  False
  CDNS          100.00                9            2.67              7.74        410.84                44.19         0.546          pass              0.502             15.7                           0.344               16.51              1.690                                 ok           False                  False
   WMT           90.00               30            0.53              0.43        114.42                32.65         0.534          pass              0.593             46.5                           0.489              -14.51             -1.671 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602094506)

</details>
