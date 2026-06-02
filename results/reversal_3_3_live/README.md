# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 12:40:04 EDT`
Last processed slot: `manage_1230`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           95.24               21            1.16              0.72         88.79                49.60         0.630          pass              0.670             44.6                           0.591               -0.54              0.187                                 ok            True                  False
  MELI           90.91               11            2.72             32.95       1716.86                60.28         0.626          pass              0.383              7.7                           0.119                6.18              0.679                                 ok            True                  False
  FTNT          100.00               29            1.36              1.40        146.54                71.69         0.619          pass              0.793             68.3                           0.734               14.73              1.266                                 ok            True                  False
  INTC           96.55               29            1.19              0.91        108.94                88.85         0.577          pass              0.809             74.8                           0.586               -0.13             -0.104                                 ok            True                  False
  AMGN           93.33               15            1.03              2.36        328.12                20.27         0.543          pass              0.595             50.6                           0.396                0.42              0.030                                 ok            True                  False
  INSM           37.50                8            4.63              3.44        104.56               110.78         0.643          pass              0.095             10.2                           0.159               -5.63             -0.354            downtrend_blocked_slope           False                  False
    ZS           50.00                4            7.88              8.59        152.03               157.27         0.562          pass              0.122             21.9                           0.683              -17.89             -2.762            downtrend_blocked_slope           False                  False
  REGN           85.19               27            1.05              4.42        598.77                42.53         0.552          pass              0.400             30.9                           0.309               -5.47             -0.653 downtrend_blocked_slope_and_streak           False                  False
   WMT           88.89               27            0.74              0.60        114.34                32.65         0.534          pass              0.556             50.9                           0.717              -14.69             -1.681 downtrend_blocked_slope_and_streak           False                  False
   HON           70.00               10            1.39              2.30        235.55                24.20         0.531          pass              0.132             26.3                           0.415                7.37              0.967                                 ok           False                  False
  PAYX           87.50                8            2.14              1.53        101.78                33.30         0.506          pass              0.384             44.4                           0.654                6.10              0.621                                 ok           False                  False
 GOOGL           87.50                8            2.44              6.42        373.62                26.14         0.503          pass              0.397             48.9                           0.536               -7.49             -0.497            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                   detail
2026-06-02T12:00:02.493429-04:00 early_entry_1200 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:55:02.481940-04:00 early_entry_1155 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:50:01.505874-04:00 early_entry_1150 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:45:06.568755-04:00 early_entry_1145 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:40:01.271913-04:00 early_entry_1140 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:35:01.271646-04:00 early_entry_1135 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:30:04.237556-04:00 early_entry_1130 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00 early_entry_1125 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "AMZN260717C00260000", "fill_price": 12.575, "pnl": 2662.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.44, "ticker": "AMZN"}
2026-06-02T11:20:04.407163-04:00 early_entry_1120 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602124004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602124004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602124004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602124004)

</details>
