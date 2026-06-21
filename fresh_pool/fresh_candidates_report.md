# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=198ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-85MS` (url=207ms, nekobox=252ms, status=yes)
3. `AKUN-003-ALIBABA-VLESS-WS-66MS` (url=215ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=217ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=198ms, nekobox=255ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=212ms, nekobox=252ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=212ms, nekobox=259ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=220ms, nekobox=252ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS` (url=210ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-118MS` (url=207ms, nekobox=186ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-231MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-230MS` (url=530ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-252MS` (url=555ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-252MS` (url=569ms, status=HTTP 204)
15. `AKUN-015-CONFLU-VLESS-WS-232MS` (url=508ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-283MS` (url=589ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-293MS` (url=561ms, status=HTTP 204)
18. `AKUN-029-UNKNOWN-VLESS-WS-491MS` (url=798ms, status=HTTP 204)
19. `AKUN-034-UNKNOWN-VLESS-WS-604MS` (url=890ms, status=HTTP 204)
20. `AKUN-035-UNKNOWN-VLESS-WS-452MS` (url=668ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
