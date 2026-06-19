# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-85MS` (url=212ms, nekobox=244ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-106MS` (url=211ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-108MS`
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-110MS`
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-122MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-247MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-271MS` (url=584ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-268MS` (url=570ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-234MS` (url=520ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-279MS` (url=7887ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-320MS` (url=580ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-233MS` (url=405ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-249MS` (url=525ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-111MS` (url=316ms, status=HTTP 204)
19. `AKUN-021-WPENG-VLESS-WS-339MS` (url=641ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-379MS` (url=579ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-394MS` (url=571ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-405MS` (url=585ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
