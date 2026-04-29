# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 10:05:08 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,922.50`
- Equity: `$17,122.50`
- Realized PnL: `$4,997.50`
- Unrealized PnL: `$2,125.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260529C00084000       2026-04-28                   1     10      7075.0                  9200.0         7.08            9.2       84.22         88.43          2125.0                  30.04         100.0               38              0.91         70.58           67.31                  91.28                 369.0           78.0               0.05                      ok
```

## Today's Closed Trades (2026-04-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           90.00               30            1.35              1.64        172.32               113.02            True
 CMCSA           91.67               24            0.60              0.12         27.60                60.29            True
  NFLX           88.89               36            0.72              0.47         92.10                46.23            True
  CDNS           86.67               15            2.58              5.87        322.82                53.80            True
  SNPS           95.83               24            2.05              6.94        480.92                50.93            True
  CRWD           81.25               32            1.22              3.88        453.33                53.30            True
  FAST           90.00               30            0.88              0.28         44.56                39.66            True
  ADSK           86.21               29            1.07              1.76        234.10                45.23            True
   HON           88.89               18            1.28              1.90        212.11                25.70            True
  DDOG           88.24               34            1.17              1.08        131.09                52.25            True
   XEL           92.59               27            0.57              0.32         79.34                20.53            True
  LRCX           81.08               37            0.51              0.90        250.85                55.21            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-29T10:05:08.240355-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-29T10:00:04.620825-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-29T09:55:04.061412-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-29T09:40:03.886159-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T09:35:04.233499-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T09:30:03.967315-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T09:25:06.961152-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T00:01:06.010136-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-28T16:10:03.932296-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-28T16:05:04.331443-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429100508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429100508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429100508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429100508)

</details>
