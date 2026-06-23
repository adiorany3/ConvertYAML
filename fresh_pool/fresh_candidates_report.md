# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 18
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=249ms, nekobox=227ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-92MS` (url=214ms, nekobox=253ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-83MS` (url=224ms, nekobox=235ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=228ms, nekobox=244ms, status=yes)
5. `AKUN-005-SPEEDTEST-VLESS-WS-117MS` (url=195ms, nekobox=181ms, status=no)
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-134MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-93MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-356MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-389MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-395MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-350MS`
12. `AKUN-013-WPENG-VLESS-WS-415MS` (url=822ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-393MS` (url=833ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-347MS` (url=756ms, status=HTTP 204)
15. `AKUN-025-CLOUDFLARE-VLESS-WS-741MS` (url=955ms, status=HTTP 204)
16. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-842MS` (url=1168ms, status=HTTP 204)
17. `AKUN-032-RS-RAPIDSEEDBOX-20190717-VLESS-WS-849MS` (url=1447ms, status=HTTP 204)
18. `AKUN-033-CLOUDFLARE-VLESS-WS-889MS` (url=1292ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
