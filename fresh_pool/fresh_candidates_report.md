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
1. `AKUN-001-MEDIUM-VLESS-WS-142MS` (url=267ms, nekobox=338ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-134MS` (url=291ms, nekobox=257ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-141MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-143MS`
5. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-142MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-138MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-147MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-148MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-148MS` (url=301ms, nekobox=356ms, status=yes)
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-161MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-148MS` (url=345ms, status=HTTP 204)
13. `AKUN-013-ADF-VLESS-WS-152MS` (url=291ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-161MS` (url=289ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-154MS` (url=281ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-186MS` (url=263ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-148MS` (url=294ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-176MS` (url=276ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-209MS` (url=307ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-158MS` (url=348ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-220MS` (url=328ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-309MS` (url=506ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-360MS` (url=702ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-348MS` (url=684ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-383MS` (url=792ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
