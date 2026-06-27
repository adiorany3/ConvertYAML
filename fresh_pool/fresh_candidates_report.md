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
1. `AKUN-001-UNKNOWN-VLESS-WS-140MS` (url=275ms, nekobox=291ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-134MS` (url=261ms, nekobox=301ms, status=yes)
3. `AKUN-003-DE-XTOM-20210903-VLESS-WS-145MS` (url=270ms, nekobox=285ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-142MS` (url=277ms, nekobox=311ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-144MS` (url=292ms, nekobox=333ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-135MS` (url=253ms, nekobox=254ms, status=no)
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-143MS`
8. `AKUN-007-ALIBABA-VLESS-WS-145MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-143MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-150MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-145MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-CLOUDWEBMANAGE-EU-FR-VLESS-WS-148MS` (url=271ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-149MS` (url=293ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-141MS` (url=265ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-141MS` (url=260ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-152MS` (url=275ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-156MS` (url=306ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-169MS` (url=260ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-143MS` (url=271ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-139MS` (url=249ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-155MS` (url=288ms, status=HTTP 204)
23. `AKUN-023-MEDIUM-VLESS-WS-155MS` (url=251ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-297MS` (url=500ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-350MS` (url=715ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
