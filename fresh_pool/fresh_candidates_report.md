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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-135MS` (url=262ms, nekobox=246ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-131MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-142MS` (url=252ms, nekobox=230ms, status=no)
4. `AKUN-002-CLOUDFLARE-VLESS-WS-150MS`
5. `AKUN-003-UNKNOWN-VLESS-WS-146MS`
6. `AKUN-006-DEV-VLESS-WS-155MS` (url=259ms, nekobox=236ms, status=no)
7. `AKUN-007-DEV-VLESS-WS-148MS` (url=269ms, nekobox=241ms, status=no)
8. `AKUN-008-UNKNOWN-VLESS-WS-151MS` (url=321ms, nekobox=241ms, status=no)
9. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-159MS`
10. `AKUN-005-UNKNOWN-VLESS-WS-170MS`
11. `AKUN-006-466688-VLESS-WS-153MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-164MS` (url=251ms, nekobox=238ms, status=no)
13. `AKUN-007-ALIBABA-VLESS-WS-153MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-141MS` (url=252ms, nekobox=239ms, status=no)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-171MS` (url=261ms, nekobox=232ms, status=no)
16. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-161MS`
17. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-166MS`
18. `AKUN-010-UNKNOWN-VLESS-WS-175MS`
19. `AKUN-019-CLOUDFLARE-VLESS-WS-172MS` (url=259ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-290MS` (url=512ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-357MS` (url=705ms, status=HTTP 204)
22. `AKUN-022-CONFLU-VLESS-WS-357MS` (url=710ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-378MS` (url=768ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-402MS` (url=757ms, status=HTTP 204)
25. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-404MS` (url=797ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
