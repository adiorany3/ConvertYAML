# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-83MS` (url=214ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=229ms, nekobox=231ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=220ms, nekobox=227ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-103MS` (url=232ms, nekobox=226ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-117MS` (url=206ms, nekobox=236ms, status=yes)
6. `AKUN-006-877774-VLESS-WS-114MS` (url=204ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-124MS` (url=197ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-124MS` (url=223ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS` (url=219ms, nekobox=236ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-144MS` (url=286ms, nekobox=306ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-159MS` (url=301ms, status=HTTP 204)
12. `AKUN-012-EE-WELCOMEHOST-20190515-VLESS-WS-164MS` (url=331ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-135MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-147MS` (url=260ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-131MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-124MS` (url=277ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-85MS` (url=201ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-307MS` (url=619ms, status=HTTP 204)
19. `AKUN-023-SUKARIO-VLESS-WS-616MS` (url=1235ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-730MS` (url=1194ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-678MS` (url=1104ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-711MS` (url=1209ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-802MS` (url=3333ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-697MS` (url=3682ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
