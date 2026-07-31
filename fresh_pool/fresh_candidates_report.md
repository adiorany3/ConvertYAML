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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-IP-VLESS-WS-86MS` (url=407ms, nekobox=298ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-92MS` (url=306ms, nekobox=386ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=343ms, nekobox=378ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS` (url=374ms, nekobox=196ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=345ms, nekobox=202ms, status=no)
6. `AKUN-004-UNKNOWN-VLESS-WS-99MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-106MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS` (url=345ms, nekobox=189ms, status=no)
9. `AKUN-006-CLOUDFLARE-VLESS-WS-117MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS` (url=314ms, nekobox=192ms, status=no)
11. `AKUN-007-UNKNOWN-VLESS-WS-127MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-120MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-163MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-153MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-177MS` (url=334ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-254MS` (url=451ms, status=HTTP 204)
17. `AKUN-018-090227-VLESS-WS-211MS` (url=366ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-360MS` (url=746ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-450MS` (url=4040ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-443MS` (url=1086ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-518MS` (url=826ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-528MS` (url=932ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-572MS` (url=5081ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-619MS` (url=1012ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-754MS` (url=1275ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
