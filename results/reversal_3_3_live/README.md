# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:40:04 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.35               34            0.58              4.17       1032.95               101.73         0.732            pass              0.504             69.4                           0.336               50.95              4.615                                 ok            True                  False
  MNST           91.67               12            1.81              1.13         88.62                49.60         0.645            pass              0.396              2.4                           0.052               -1.19              0.157                                 ok            True                  False
  MELI           91.67               24            1.85             22.46       1721.36                60.28         0.597            pass              0.575             37.1                           0.462                7.12              0.719                                 ok            True                  False
  INTC           96.00               25            1.91              1.46        108.70                88.85         0.554            pass              0.734             59.5                           0.670               -0.86             -0.137                                 ok            True                  False
  AMGN           93.33               15            1.02              2.36        328.12                20.27         0.544            pass              0.595             50.7                           0.709                0.42              0.030                                 ok            True                  False
  CDNS           88.89               18            2.06              5.98        411.60                44.19         0.509            pass              0.446             34.9                           0.381               17.23              1.719                                 ok            True                  False
 CMCSA           83.33               18            1.12              0.20         24.97                17.46         0.500 below_threshold              0.226             11.1                           0.215               -0.64              0.012                                 ok            True                  False
  FTNT          100.00                9            2.21              2.27        146.17                71.69         0.695            pass              0.615             48.6                           0.594               13.75              1.226                                 ok           False                  False
  INSM           50.00               12            3.92              2.91        104.78               110.78         0.676            pass              0.153             23.9                           0.388               -4.93             -0.320            downtrend_blocked_slope           False                  False
    ZS          100.00                2            8.85              9.65        151.58               157.27         0.576            pass              0.479              7.1                           0.184              -18.75             -2.810            downtrend_blocked_slope           False                  False
   WMT           82.35               17            1.25              1.00        114.17                32.65         0.560            pass              0.217             17.3                           0.265              -15.13             -1.704 downtrend_blocked_slope_and_streak           False                  False
  REGN           87.10               31            0.78              3.29        599.25                42.53         0.546            pass              0.530             48.6                           0.472               -5.21             -0.641 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                 detail
2026-06-02T10:40:04.457109-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:35:04.553797-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:30:04.405006-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:25:01.235572-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:20:01.327977-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015 entry_candidate_skipped {"early_entry_score": 0.679, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 117.0, "option_spread_pct": 24.24, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.442}
2026-06-02T10:10:06.260122-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:05:01.451088-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:00:02.499087-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602104004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602104004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602104004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602104004)

</details>
