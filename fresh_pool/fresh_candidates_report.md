# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=236ms, nekobox=263ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=221ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=252ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=230ms, nekobox=267ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=240ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=279ms, nekobox=291ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-101MS` (url=290ms, nekobox=255ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-81MS` (url=252ms, nekobox=285ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=238ms, nekobox=264ms, status=yes)
10. `AKUN-010-UK-GB-DCL-01-20191003-VLESS-WS-120MS` (url=266ms, nekobox=289ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-104MS` (url=261ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=242ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-262MS` (url=551ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-265MS` (url=676ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-298MS` (url=675ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-291MS` (url=659ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-303MS` (url=650ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-276MS` (url=583ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-310MS` (url=611ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-335MS` (url=617ms, status=HTTP 204)
21. `AKUN-032-UNKNOWN-VLESS-WS-634MS` (url=904ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
