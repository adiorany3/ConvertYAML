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
1. `AKUN-001-UNKNOWN-VLESS-WS-78MS` (url=229ms, nekobox=263ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=227ms, nekobox=257ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-82MS` (url=229ms, nekobox=252ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-86MS` (url=224ms, nekobox=348ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=210ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS` (url=230ms, nekobox=244ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=207ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=224ms, nekobox=228ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=201ms, nekobox=230ms, status=yes)
10. `AKUN-010-CZ-LOTUNA-19970206-VLESS-WS-108MS` (url=230ms, nekobox=255ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-105MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-114MS` (url=207ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-116MS` (url=204ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-118MS` (url=202ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-110MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-121MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-109MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-110MS` (url=257ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-102MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-120MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-138MS` (url=206ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-136MS` (url=236ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-129MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-145MS` (url=298ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-97MS` (url=227ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
