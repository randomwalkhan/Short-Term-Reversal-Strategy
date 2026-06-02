# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 11:40:01 EDT`
Last processed slot: `manage_1130`

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
  FTNT          100.00               13            1.99              2.05        146.26                71.69         0.684          pass              0.650             53.7                           0.576               14.00              1.237                                 ok            True                  False
  MNST           95.00               20            1.31              0.82         88.75                49.60         0.626          pass              0.642             37.4                           0.502               -0.69              0.180                                 ok            True                  False
  MELI           90.91               22            2.01             24.37       1720.54                60.28         0.599          pass              0.526             31.7                           0.378                6.95              0.712                                 ok            True                  False
  INTC           96.67               30            1.10              0.84        108.97                88.85         0.577          pass              0.821             76.7                           0.648               -0.04             -0.099                                 ok            True                   True
  AMGN           88.24               17            0.97              2.23        328.18                20.27         0.527          pass              0.479             53.4                           0.367                0.48              0.033                                 ok            True                  False
  ROST           93.33               30            0.71              1.11        223.59                42.05         0.506          pass              0.776             79.0                           0.378                5.40              0.675                                 ok            True                  False
   ADP          100.00               14            2.13              3.48        232.25                34.26         0.503          pass              0.602             41.7                           0.707                2.62              0.311                                 ok            True                  False
  INSM           44.44                9            4.30              3.19        104.66               110.78         0.665          pass              0.116             16.6                           0.194               -5.30             -0.338            downtrend_blocked_slope           False                  False
   WMT           76.92               13            1.40              1.12        114.12                32.65         0.572          pass              0.100              7.5                           0.160              -15.25             -1.711 downtrend_blocked_slope_and_streak           False                  False
    ZS          100.00                2            9.14              9.96        151.44               157.27         0.549          pass              0.483              9.4                           0.406              -19.01             -2.825            downtrend_blocked_slope           False                  False
  REGN           88.24               34            0.69              2.90        599.42                42.53         0.532          pass              0.597             54.6                           0.370               -5.13             -0.636 downtrend_blocked_slope_and_streak           False                  False
   HON           72.73               11            1.36              2.25        235.57                24.20         0.529          pass              0.143             27.9                           0.435                7.41              0.969                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                   detail
2026-06-02T11:40:01.271913-04:00 early_entry_1140 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:35:01.271646-04:00 early_entry_1135 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:30:04.237556-04:00 early_entry_1130 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00 early_entry_1125 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:25:01.418868-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "AMZN260717C00260000", "fill_price": 12.575, "pnl": 2662.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.44, "ticker": "AMZN"}
2026-06-02T11:20:04.407163-04:00 early_entry_1120 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:15:04.236525-04:00 early_entry_1115 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:10:04.323542-04:00 early_entry_1110 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:05:01.381854-04:00 early_entry_1105 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
2026-06-02T11:00:04.363054-04:00 early_entry_1100 entry_skipped                                                                                                                                                          {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602114001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602114001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602114001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602114001)

</details>
