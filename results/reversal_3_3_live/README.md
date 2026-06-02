# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 09:40:02 EDT`
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
    MU           82.35               34            0.61              4.42       1032.85               101.73         0.749          pass              0.500             67.6                           0.368               50.90              4.613                                 ok            True                  False
  MELI           92.31               26            1.59             19.22       1722.74                60.28         0.610          pass              0.584             29.5                           0.352                7.42              0.732                                 ok            True                  False
  CDNS           93.75               16            2.12              6.14        411.53                44.19         0.529          pass              0.543             27.9                           0.461               17.17              1.716                                 ok            True                  False
  UPRO           93.75               32            0.59              0.62        150.06                29.00         0.518          pass              0.725             53.2                           0.512                7.23              0.921                                 ok            True                  False
   ADP          100.00               10            2.53              4.15        231.96                34.26         0.512          pass              0.494             14.4                           0.238                2.19              0.292                                 ok            True                  False
  AMGN           87.50               24            0.72              1.66        328.42                20.27         0.505          pass              0.424             26.9                           0.346                0.73              0.044                                 ok            True                  False
  FTNT          100.00                9            2.60              2.68        145.99                71.69         0.672          pass              0.585             39.4                           0.619               13.29              1.208                                 ok           False                  False
  INSM           37.50                8            4.55              3.37        104.58               110.78         0.653          pass              0.075              3.2                           0.131               -5.54             -0.350            downtrend_blocked_slope           False                  False
    ZS           50.00                4            7.77              8.47        152.08               157.27         0.592          pass              0.079              6.5                           0.223              -17.79             -2.757            downtrend_blocked_slope           False                  False
  SHOP           72.73               22            2.88              2.51        123.05                84.68         0.583          pass              0.203             21.5                           0.303               17.73              2.025                                 ok           False                  False
  REGN           88.57               35            0.49              2.05        599.78                42.53         0.547          pass              0.583             44.2                           0.342               -4.93             -0.627 downtrend_blocked_slope_and_streak           False                  False
  MNST           97.83               46            0.17              0.11         89.05                49.60         0.545          pass              0.883             76.2                           0.392                0.46              0.233                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602094002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602094002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602094002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602094002)

</details>
