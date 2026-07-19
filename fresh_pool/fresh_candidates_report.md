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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=204ms, nekobox=232ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-89MS` (url=213ms, nekobox=245ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-87MS` (url=202ms, nekobox=231ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=202ms, nekobox=249ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS` (url=204ms, nekobox=230ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS` (url=204ms, nekobox=237ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=202ms, nekobox=228ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS` (url=202ms, nekobox=237ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-117MS` (url=245ms, nekobox=335ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-89MS` (url=286ms, nekobox=241ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-94MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-94MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-UK-GB-DCL-01-20191003-VLESS-WS-130MS` (url=264ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-133MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-122MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-134MS` (url=270ms, status=HTTP 204)
18. `AKUN-018-ZOOM-VLESS-WS-94MS` (url=219ms, status=HTTP 204)
19. `AKUN-019-POLICE-VLESS-WS-138MS` (url=247ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-165MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-170MS` (url=261ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-114MS` (url=281ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-376MS` (url=807ms, status=HTTP 204)
24. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-368MS` (url=788ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-315MS` (url=2584ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
