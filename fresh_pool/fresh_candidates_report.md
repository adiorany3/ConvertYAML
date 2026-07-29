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
1. `AKUN-001-UNKNOWN-VLESS-WS-52MS` (url=385ms, nekobox=389ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=386ms, nekobox=410ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=371ms, nekobox=398ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=357ms, nekobox=429ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-70MS` (url=359ms, nekobox=386ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-56MS` (url=350ms, nekobox=399ms, status=yes)
7. `AKUN-007-ZOOM-VLESS-WS-67MS` (url=382ms, nekobox=392ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-78MS` (url=363ms, nekobox=380ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-96MS` (url=204ms, nekobox=334ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=194ms, nekobox=233ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-104MS` (url=680ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-141MS` (url=684ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-74MS` (url=374ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-69MS` (url=360ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-225MS` (url=388ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-227MS` (url=368ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-127MS` (url=710ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-97MS` (url=400ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=371ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-99MS` (url=707ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-516MS` (url=1107ms, status=HTTP 204)
22. `AKUN-026-090227-VLESS-WS-516MS` (url=995ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-58MS` (url=1188ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-268MS` (url=1871ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
