# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-008500-VLESS-WS-137MS` (url=304ms, nekobox=291ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-137MS` (url=268ms, nekobox=306ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-149MS` (url=288ms, nekobox=313ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-154MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-151MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-146MS` (url=270ms, nekobox=243ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-160MS`
8. `AKUN-009-CLOUDFLARE-VLESS-WS-151MS` (url=283ms, nekobox=256ms, status=no)
9. `AKUN-007-WPENG-VLESS-WS-143MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-166MS` (url=271ms, nekobox=312ms, status=no)
11. `AKUN-008-CLOUDWEBMANAGE-EU-FR-VLESS-WS-156MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-171MS`
13. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS`
14. `AKUN-015-UNKNOWN-VLESS-WS-188MS` (url=336ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-182MS` (url=332ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-182MS` (url=288ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-147MS` (url=302ms, status=HTTP 204)
18. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-175MS` (url=300ms, status=HTTP 204)
19. `AKUN-020-008500-VLESS-WS-153MS` (url=263ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-373MS` (url=684ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-155MS` (url=295ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-380MS` (url=717ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-406MS` (url=726ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-420MS` (url=736ms, status=HTTP 204)
25. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-393MS` (url=742ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
